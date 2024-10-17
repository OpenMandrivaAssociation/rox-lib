%define name rox-lib
%define version 2.0.6
%define release 2
%define oname rox-lib2
Summary: Shared code for ROX applications
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/rox/%{oname}-%{version}.tar.bz2
License: LGPL
Group: Graphical desktop/Other
URL: https://rox.sourceforge.net/rox_lib.html
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



%changelog
* Wed Mar 16 2011 StÃ©phane TÃ©letchÃ©a <steletch@mandriva.org> 2.0.6-1mdv2011.0
+ Revision: 645418
- update to new version 2.0.6

* Tue Sep 08 2009 Thierry Vignaud <tv@mandriva.org> 2.0.5-5mdv2010.0
+ Revision: 433389
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 2.0.5-4mdv2009.0
+ Revision: 260298
- rebuild

* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 2.0.5-3mdv2009.0
+ Revision: 251376
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Nov 09 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.5-1mdv2008.1
+ Revision: 107239
- new version

* Thu Jul 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.4-2mdv2008.0
+ Revision: 51540
- never use libdir in a noarch package

* Mon May 28 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.0.4-1mdv2008.0
+ Revision: 32084
- new version


* Mon May 29 2006 Götz Waschk <waschk@mandriva.org> 2.0.3-1mdv2007.0
- New release 2.0.3
- use mkrel

* Mon Aug 01 2005 Götz Waschk <waschk@mandriva.org> 2.0.2-1mdk
- New release 2.0.2

* Sun Jul 10 2005 Götz Waschk <waschk@mandriva.org> 2.0.1-1mdk
- New release 2.0.1

* Mon Apr 18 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 2.0.0-1mdk
- New release 2.0.0

* Sat Mar 26 2005 GÃ¶tz Waschk <waschk@linux-mandrake.com> 1.9.18-1mdk
- New release 1.9.18

* Fri Jan 21 2005 Goetz Waschk <waschk@linux-mandrake.com> 1.9.17-1mdk
- New release 1.9.17

* Sun Oct 03 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.9.16-1mdk
- New release 1.9.16

* Sun Aug 29 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.15-1mdk
- fix source URL
- New release 1.9.15

* Sat Apr 17 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.14-1mdk
- new version

* Fri Apr 02 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.13-1mdk
- new version

* Fri Jan 23 2004 Götz Waschk <waschk@linux-mandrake.com> 1.9.12-1mdk
- new version

* Wed Oct 15 2003 Götz Waschk <waschk@linux-mandrake.com> 1.9.11-1mdk
- new version

* Sat Oct 04 2003 Götz Waschk <waschk@linux-mandrake.com> 1.9.10-1mdk
- new version

* Sun Aug 17 2003 Götz Waschk <waschk@linux-mandrake.com> 1.9.9-1mdk
- drop prefix
- new version

* Sat Jul 19 2003 Götz Waschk <waschk@linux-mandrake.com> 1.9.8-1mdk
- new version

