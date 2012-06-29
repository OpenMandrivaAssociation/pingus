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
Patch0:		pingus-0.7.6-fix-wiimote-driver-build.patch
Patch1:		pingus-0.7.6-fix-file-permissions.patch
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
%patch0 -p1 -b .wiimote~
%patch1 -p1 -b .perms~

%build
# XXX: passing of flags through CXXFLAGS etc. is fscked..
%scons \
	prefix=%{_prefix} \
	execprefix=%{_gamesbindir} \
	datadir=%{_gamesdatadir} \
	with_wiimote=True \
	CC="gcc %{optflags} %{ldflags}" \
	CXX="g++ %{optflags} %{ldflags}" \
	CCFLAGS="-Ofast" \
	CXXFLAGS="-Ofast"

%install
%makeinstall_std \
	DATADIR=%{_gamesdatadir}/%{name} \
	MANDIR=%{_mandir} \
	BINDIR=%{_gamesbindir} \
	LIBDIR=%{_gameslibdir}


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

sed -i "s^%{buildroot}/^^g" %{buildroot}%{_gamesbindir}/pingus

%files
%doc AUTHORS COPYING README* TODO
%{_gamesbindir}/pingus
%{_gamesbindir}/pingus.bin
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/pingus.6.*
