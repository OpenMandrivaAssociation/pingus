%define	name	pingus
%define	version	0.7.2
%define	release	1
%define	Summary	Pingus - A free Lemmings clone

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Source0:	http://dark.x.dtu.dk/~grumbel/pingus/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch1:		pingus-0.7.1-dataloc.patch
Patch2:		pingus-0.7.1-boost.patch
URL:		http://pingus.seul.org/
License:	GPLv2+
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	scons
BuildRequires:	boost-devel
BuildRequires:	SDL_mixer-devel 
BuildRequires:	SDL_image-devel
BuildRequires:	libpng-devel
BuildRequires:	physfs-devel

%description
Pingus is a free Lemmings clone covered under the GPL. Pingus uses SDL,
which should make it portable over a lot of operating systems in the future. At
the moment the main target is Linux. It is possible to play Pingus in a X
window or in fullscreen.

%prep
%setup -q
%patch1 -p1 -b .dataloc
%patch2 -p0 -b .boost
sed -i 's/BINDIR="\$1\/bin\/"/BINDIR="\$1\/games"/' install.sh
sed -i 's/DATADIR="\$1\/share\/pingus\/"/DATADIR="\$1\/share\/games\/pingus\/"/' install.sh
%build
scons

%install
rm -rf $RPM_BUILD_ROOT
./install.sh $RPM_BUILD_ROOT/usr

install -m 755 -d $RPM_BUILD_ROOT%{_datadir}/applications/
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
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
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
