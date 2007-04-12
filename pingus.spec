%define	name	pingus
%define	version	0.6.0
%define	release	%mkrel 9
%define	Summary	Pingus - A free Lemmings clone

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://dark.x.dtu.dk/~grumbel/pingus/%{name}-%{version}.tar.bz2
Source3:	pingus-music-0.4.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		pingus-0.6.0-gcc33.patch
Patch1:		pingus-0.6.0-gcc34.patch
Patch2:		pingus-0.6.0-gcc401.patch
URL:		http://pingus.seul.org/
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ImageMagick-devel clanlib0.6-devel libclanlib-jpeg
BuildRequires:	libclanlib-png libclanlib-vorbis esound-devel 
BuildRequires:	tiff-devel SDL_mixer-devel libxml2-devel
BuildRequires:	libclanlib-mikmod libclanlib-gui libclanlib-sound
# (gc) needed because of binary incompatibility of datafiles between versions of clanlib
Requires:	clanlib0.6 = 0.6.5

%description
Pingus is a free Lemmings clone covered under the GPL. Pingus uses ClanLib,
which should make it portable over a lot of operating systems in the future. At
the moment the main target is Linux. It is possible to play Pingus in a X
window or in fullscreen using DGA or fbdev.

%prep
%setup -q
%patch0 -p1 -b .gcc33
%patch1 -p0 -b .gcc34
%patch2 -p0 -b .gcc401

%build
%configure2_5x --bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall bindir=$RPM_BUILD_ROOT%{_gamesbindir}

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" icon="%{name}.png" \
  needs="x11" section="More Applications/Amusement/Arcade" title="Pingus" \
  longtitle="%{Summary}" xdg=true
EOF
install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Pingus
Comment=%Summary
Exec=%{_gamesbindir}/%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/games/%{name}/
tar jxvf %{SOURCE3} -C $RPM_BUILD_ROOT%{_datadir}/games/%{name}/
rm -f $RPM_BUILD_ROOT%{_datadir}/games/%{name}/*/.cvsignore
# (gc) very rough
mv $RPM_BUILD_ROOT%{_datadir}/games/%{name}/{pingus-music-0.4,music}

#mkdir -p $RPM_BUILD_ROOT%{_datadir}/games/%{name}/sound
#tar jxvf %{SOURCE4} -C $RPM_BUILD_ROOT%{_datadir}/games/%{name}/sound

%find_lang %{name}

rm -f $RPM_BUILD_ROOT%{_datadir}/locale/locale.alias

%post
%{update_menus}
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README* TODO
%{_gamesbindir}/pingus
%{_mandir}/*/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png


