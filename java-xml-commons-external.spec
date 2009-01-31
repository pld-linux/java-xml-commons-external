# TODO
# - something with org.apache.env.which (currently xml-commons-which.jar in
#   xml-commons), then obsolete xml-commons here
%include	/usr/lib/rpm/macros.java
Summary:	Apache XML Commons External classes
Summary(pl.UTF-8):	Klasy Apache XML Commons External
Name:		xml-commons-external
Version:	1.3.04
Release:	2
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/xml/commons/%{name}-%{version}-src.tar.gz
# Source0-md5:	5536f87a816c766f4999ed60593a8701
# from http://svn.apache.org/repos/asf/xml/commons/trunk/java/external/build.xml
Source1:	%{name}-build.xml
URL:		http://xml.apache.org/commons/
BuildRequires:	ant
BuildRequires:	java-gcj-compat
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache XML Commons External classes:
 - DOM Level 3 from w3c.org
 - SAX 2.0 from megginson.com

%description -l pl.UTF-8
Klasy Apache XML Commons External:
 - DOM Level 3 z w3c.org
 - SAX 2.0 z megginson.com

%package javadoc
Summary:	javadoc documentation for Apache XML Commons External
Summary(pl.UTF-8):	Dokumentacja javadoc dla pakietu Apache XML Commons External
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
javadoc documentation for Apache XML Commons External.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc dla pakietu Apache XML Commons External.

%prep
%setup -q -c
cp %{SOURCE1} build.xml

# for build.xml
mkdir src xdocs
ln -s ../javax ../org ../manifest.commons src

%build
# default 64m is too low
#export ANT_OPTS="-Xmx128m"
%ant jar javadoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install build/xml-apis.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis-%{version}.jar
install build/xml-apis-ext.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis-ext-%{version}.jar
ln -s xml-apis-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis.jar
ln -s xml-apis-ext-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/xml-apis-ext.jar

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -a build/docs/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%doc LICENSE* NOTICE README.*
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
