# Build is broken at least is 0.7.6, 
# missing #include "pingus/debug.hpp
%define build_extra_input 0

Summary:	Pingus - A free Lemmings clone
Name:		pingus
Version:	0.7.6
Release:	2
License:	GPLv2+
Group:		Games/Arcade
URL:		http://pingus.seul.org
Source0:	http://pingus.googlecode.com/files/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		pingus-0.7.6-gcc470-udl.patch
BuildRequires:	scons
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(xi)
BuildRequires:	physfs-devel
BuildRequires:	cwiid-devel
# To avoid automatic Requires on file
BuildRequires:	guile

%description
Pingus is a free Lemmings clone covered under the GPL. Pingus uses SDL,
which should make it portable over a lot of operating systems in the future. At
the moment the main target is Linux. It is possible to play Pingus in a X
window or in fullscreen.

%prep
%setup -q
%patch0 -p0

%build
%scons \
%if %{build_extra_input}
	with_xinput=true \
    with_wiimote=true \
%endif
	prefix=%{_prefix} \
	execprefix=%{_gamesbindir} \
	datadir=%{_gamesdatadir} \
	libdir=%{_libdir}

%install
%makeinstall \
	DATADIR=%{buildroot}/%{_gamesdatadir}/%{name} \
	MANDIR=%{buildroot}/%{_mandir} \
	BINDIR=%{buildroot}/%{_gamesbindir} \
	LIBDIR=%{buildroot}/%{_libdir}


install -m 755 -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Pingus
Comment=A free Lemmings clone
Exec=%{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

rm -f %{buildroot}%{_datadir}/locale/locale.alias

sed -i "s^%{buildroot}/^^g" %{buildroot}%{_gamesbindir}/pingus

%files
%doc AUTHORS COPYING README* TODO
%{_gamesbindir}/pingus
%{_gamesbindir}/pingus.bin
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/pingus.6.*


%changelog
* Wed Jan 25 2012 Zombie Ryushu <ryushu@mandriva.org> 0.7.6-1
+ Revision: 768176
- Update to 0.7.6

* Wed Oct 26 2011 Götz Waschk <waschk@mandriva.org> 0.7.5-1
+ Revision: 707265
- new version
- remove old patches
- fix paths wrapper script
- spec cleanup

  + Zombie Ryushu <ryushu@mandriva.org>
    - fix man page

* Thu Oct 13 2011 Zombie Ryushu <ryushu@mandriva.org> 0.7.4-1
+ Revision: 704547
- Fix a buinch of stuff
- deprecate old patches
- Upgrade to 0.7.4

* Wed Mar 16 2011 Funda Wang <fwang@mandriva.org> 0.7.3-4
+ Revision: 645383
- rebuild for new boost

* Sun Aug 29 2010 Funda Wang <fwang@mandriva.org> 0.7.3-3mdv2011.0
+ Revision: 574093
- rebuild

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 0.7.3-2mdv2011.0
+ Revision: 566295
- rebuild for new boost

* Thu Jul 29 2010 Zombie Ryushu <ryushu@mandriva.org> 0.7.3-1mdv2011.0
+ Revision: 562909
- Upgrade to 0.7.3
- Upgrade to 0.7.3

* Tue Jun 29 2010 Pascal Terjan <pterjan@mandriva.org> 0.7.2-8mdv2010.1
+ Revision: 549480
- Add BuildRequires guile (#53526)

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 0.7.2-7mdv2010.1
+ Revision: 501882
- rebuild for new boost

* Wed Feb 03 2010 Funda Wang <fwang@mandriva.org> 0.7.2-6mdv2010.1
+ Revision: 500309
- rebuild for new boost

* Tue Jan 05 2010 Thierry Vignaud <tv@mandriva.org> 0.7.2-5mdv2010.1
+ Revision: 486394
- rebuild with latest spec-helper which add package require instead of file
  require due to scripts using guile (#55407)

* Fri Aug 21 2009 Funda Wang <fwang@mandriva.org> 0.7.2-4mdv2010.0
+ Revision: 418846
- sync with fedora gcc44 patch

* Mon Mar 09 2009 Emmanuel Andry <eandry@mandriva.org> 0.7.2-3mdv2009.1
+ Revision: 353225
- add wiimote support

* Sun Dec 21 2008 Funda Wang <fwang@mandriva.org> 0.7.2-2mdv2009.1
+ Revision: 316922
- rebuild for new boost

* Tue Sep 02 2008 Emmanuel Andry <eandry@mandriva.org> 0.7.2-1mdv2009.0
+ Revision: 279350
- add gcc43 patch

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 04 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.2-1mdv2008.1
+ Revision: 105757
- spec file clean
- move icons to the fd.o icons directory
- add scriplets
- compile with support for wiimote
- drop patch 2
- compile with optflags
- drop X-MandrivaLinux away from desktop file
- new version
- new license policy

* Fri Oct 26 2007 Crispin Boylan <crisb@mandriva.org> 0.7.1-2mdv2008.1
+ Revision: 102297
- Update description, update and reenable patch1

* Thu Oct 25 2007 Crispin Boylan <crisb@mandriva.org> 0.7.1-1mdv2008.1
+ Revision: 102209
- Add patch2 for new boost lib name
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Aug 28 2007 Crispin Boylan <crisb@mandriva.org> 0.7.0-1mdv2008.0
+ Revision: 72333
- New version, does not depend on clanlib anymore


* Sat Jan 06 2007 Götz Waschk <waschk@mandriva.org> 0.6.0-9mdv2007.0mdv2007.0
+ Revision: 104768
- Import pingus

* Sat Jan 06 2007 Götz Waschk <waschk@mandriva.org> 0.6.0-9mdv2007.1mdv2007.1
- unpack patches
- xdg menu

* Mon Jan 16 2006 Olivier Blin <oblin@mandriva.com> 0.6.0-9mdk
- buildrequires correct clanlib version

* Wed Dec 21 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.6.0-8mdk
- from Colin Guthrie <mdk@colin.guthr.ie> :
	o fix build with gcc4 (P2)
	o remove locale.alias which breaks build

* Wed Sep 01 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.0-7mdk
- rebuild for new menu
- fix buildrequires (lib64..)

* Tue Jun 29 2004 Michael Scherer <misc@mandrake.org> 0.6.0-6mdk
- rebuild for new gcc and new clanlib, with the help of Laurent Montel <lmontel@mandrakesoft.com>
- remove Packager tag

