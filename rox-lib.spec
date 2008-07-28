%define name rox-lib
%define version 2.0.5
%define release %mkrel 3
%define oname rox-lib2
Summary: Shared code for ROX applications
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/rox/%{oname}-%{version}.tar.bz2
License: LGPL
Group: Graphical desktop/Other
URL: http://rox.sourceforge.net/rox_lib.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: pygtk2.0
Requires: rox

%description
There is quite a lot of code which is needed by many ROX applications -- for
example: save boxes, menus and options.

Keeping all this code in one place makes these programs smaller. It also
makes programs which use it more consistant.

Programs which use ROX-Lib2 need to be able to find it, so you should put it
inside one of the standard library directories. If you don't have root
access, create a directory called 'lib' inside your home directory and move
ROX-Lib2 in there.


%prep
%setup -q -n %oname-%version
chmod 644 */*.xml

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_prefix/lib
cp -r ROX-Lib2 %buildroot/%_prefix/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ROX-Lib2/Help/README
%_prefix/lib/ROX-Lib2

