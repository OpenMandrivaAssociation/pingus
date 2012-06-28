%define	Summary	Pingus - A free Lemmings clone

Summary:	%{Summary}
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
BuildRequires:	scons
BuildRequires:	boost-devel
BuildRequires:	SDL_mixer-devel 
BuildRequires:	SDL_image-devel
BuildRequires:	libpng-devel
BuildRequires:	physfs-devel
BuildRequires:	cwiid-devel
BuildRequires:	bluez-devel >= 4.101-3
# To avoid automatic Requires on file
BuildRequires:	guile

%description
Pingus is a free Lemmings clone covered under the GPL. Pingus uses SDL,
which should make it portable over a lot of operating systems in the future. At
the moment the main target is Linux. It is possible to play Pingus in a X
window or in fullscreen.

%prep
%setup -q

# sed -i 's/BINDIR="\$1\/bin\/"/BINDIR="\$1\/games"/' install.sh
# sed -i 's/DATADIR="\$1\/share\/pingus\/"/DATADIR="\$1\/share\/games\/pingus\/"/' install.sh

%build
%scons \
	prefix=%{_prefix} \
	execprefix=%{_gamesbindir} \
	datadir=%{_gamesdatadir} \
	libdir=%{_gameslibdir} \
	with_wiimote=True

%install
%makeinstall \
	DATADIR=%{buildroot}%{_gamesdatadir}/%{name} \
	MANDIR=%{buildroot}%{_mandir} \
	BINDIR=%{buildroot}%{_gamesbindir} \
	LIBDIR=%{buildroot}%{_gameslibdir}


install -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Pingus
Comment=%{Summary}
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

# %find_lang %{name}

rm -f %{buildroot}%{_datadir}/locale/locale.alias

sed -i "s^%{buildroot}/^^g" %{buildroot}%{_gamesbindir}/pingus


%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files
# -f %{name}.lang
%doc AUTHORS COPYING README* TODO
%{_gamesbindir}/pingus
%{_gamesbindir}/pingus.bin
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/pingus.6.*
