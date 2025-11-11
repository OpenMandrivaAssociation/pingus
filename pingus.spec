%define __scm git
# Build is broken at least is 0.7.6, 
# missing #include "pingus/debug.hpp
%define build_extra_input 0
%undefine _debugsource_packages

Summary:	A free Lemmings clone
Name:		pingus
Version:	0.7.6
Release:	6
License:	GPLv2+
Group:		Games/Arcade
URL:		https://pingus.seul.org/
Source0:	https://github.com/Pingus/pingus/archive/refs/tags/v%{version}.tar.gz
Source1:	https://github.com/logmich/logmich/archive/refs/heads/logmich-0.1.x.tar.gz
Source2:	https://github.com/tinygettext/tinygettext/archive/refs/heads/master.tar.gz#/tinygettext.tar.gz
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
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
BuildRequires:	git-core
# To avoid automatic Requires on file
BuildRequires:	guile

%patchlist
0001-Applied-MacOSX-patch-from-Jonas-B-hr-jonas.baehr-web.patch
0002-edited-userdir-for-osx.patch
0003-Added-bytesPerPixel-to-image-info.patch
0004-Use-resource_path-data-instead-of-just-data-for-MacO.patch
0005-Compiles-on-OSX-again-looks-for-data-directly-in-Res.patch
0006-More-files-to-allow-for-MacOS-X-bundling.patch
0007-Fixed-rypo-in-mac-script.patch
0008-On-OSX-ping-can-be-launch-from-source-directory-agai.patch
0009-Alot-of-code-cleanups-relating-to-OSX-by-Jonas.patch
0010-Fixedn-typo-in-datadir.patch
0011-Added-RGBA-blitter.patch
0012-Added-blitter-test-level.patch
0013-Added-remove-blitter-for-RGBA.patch
0014-Used-RGBAmask-and-RGBAshift-instead-of-assuming-a-ha.patch
0015-Added-Jonas-B-hr-and-Josh-Dye-to-credits.patch
0016-mac-srcipt-creates-DMG.patch
0017-Changed-image-info-to-print-info-on-RGBAmask-shift-l.patch
0018-Only-use-RGBA-blitter-when-alpha-channel-is-present.patch
0019-Spelling-fix.patch
0020-Attach-license-to-DMG-files.patch
0021-Made-Makefile.macosx-add-COPYING-and-AUTHORS-to-the-.patch
0022-update-translations-from-launchpad.patch
0023-Added-eyeland-levels-from-wuzzy2-mail.ru-needs-some-.patch
0024-Lock-xmas-levels-by-default.patch
0025-German-translation-updates-by-wuzzy2-mail.ru.patch
0026-Added-framework-Cocoa-as-requested-by-Josh-Dye.patch
0027-Update-to-zh_TW-from-cges30901-gmail.com.patch
0028-update-translation-from-launchpad-added-lt.po-ca.po.patch
0029-Applied-C-11-patch-from-Kasper-Laudrup-laudrup-stack.patch
0030-Added-level-by-Yann-MRN.patch
0031-partial-fix-130-Invisible-russian-letters-png-font-i.patch
0032-update-fonts-README-fix-advance-16-to-22-in-fonts-ch.patch
0033-added-Galician-Language.patch
0034-Added-support-for-the-XDG-Base-Directory-Specificati.patch
0035-Throw-an-exception-when-Surface-creation-fails-inste.patch
0036-Add-Scottish-Gaelic-translation-by-F-ram-na-G-idhlig.patch
0037-added-level-by-Georg.rieger-georg.rieger-eblcom.ch.patch
0038-Update-scripts-to-attach-SLA-to-DMG-to-work-with-10..patch
0039-Added-two-levels-by-Katharina-Bock-bock.ka26-yahoo.d.patch
0040-Added-level-from-georg.rieger-eblcom.ch.patch
0041-fixed-untranslable-string-in-editor-update-translati.patch
0042-added-old-to-.gitignore.patch
0043-Fixed-some-compiler-warnings.patch
0044-Fixed-mixup-in-Rect-class.patch
0045-Improved-error-message-on-surface-load-failure.patch
0046-Improved-error-message.patch
0047-Added-new-levels-by-Jiri-Casek-jiricasek-gmail.com.patch
0048-More-levels-from-jiricasek-gmail.com.patch
0049-Added-missing-to-the-generated-pingus-start-script.patch
0050-Added-new-levels-from-Cameron-Barratt-barrattcb-gmai.patch
0051-Fixed-filenames-and-author-tags.patch
0052-level-fix-by-Tom-Flavel-tom-printf.net.patch
0053-Polish-translation-update-by-Marcin-Kocur-marcin2006.patch
0054-fix-line-too-long-in-pl.po-by-Marcin-Kocur.patch
0055-Added-new-levels-from-Cameron-Barratt-barrattcb-gmai.patch
0056-changes-to-deset7-by-Cameron-Barratt-barrattcb-gmail.patch
0057-fix-nn.po-by-Karl-Ove-Hufthammer-karl-huftis.org.patch
0058-Added-new-levels-from-Cameron-Barratt-barrattcb-gmai.patch
0059-Added-new-levels-from-Cameron-Barratt-barrattcb-gmai.patch
0060-new-levelset-with-all-levels-by-cbarratt.patch
0061-Added-new-levels-from-Cameron-Barratt-barrattcb-gmai.patch
0062-update-Lithuanian-translation-launchpad-934057.patch
0063-level-fix-from-Cameron-Barratt-barrattcb-gmail.com.patch
0064-level-review-by-Cameron-Barratt-barrattcb-gmail.com.patch
0065-Added-new-level-from-Afeef-Ahmed-afeefmaloram-gmail..patch
0066-add-level-by-Lina-Wiggers-lina-wiggers.org.patch
0067-added-level-by-Richard-Qian-richwiki101-gmail.com.patch
0068-added-space-adventure.levelset.patch
0069-Add-the-locked-f-flag.patch
0070-Fixed-compiler-warning-in-tinygettext.patch
0071-Switched-to-boost-signals2.patch
0072-Fixed-some-Werror-conversion-issues.patch
0073-Added-logmich-library.patch
0074-Added-logmich-to-external-README.patch
0075-Added-logmich-includes.patch
0076-Updated-logmich.patch
0077-Switched-source-over-to-logmich-s-format-string-base.patch
0078-A-new-levelset-by-Shaun-David-Crowdus-maestrochesher.patch
0079-Removed-trailing-whitespace.patch
0080-Removed-external-logmich-and-external-tinygettext.patch
0081-Added-external-logmich-and-external-tinygettext-as-g.patch
0082-Updated-tinygettext-include-path.patch
0083-Fixes-141.patch
0084-Converted-README-to-README.md.patch
0085-Moved-TODO-to-wiki.patch
0086-Fix-build-when-wiimote-is-enabled.patch
0087-Fix-build-when-xinput-is-enabled.patch
0088-Fix-exception-on-creation-of-directory-hierachies.patch
0090-Fix-wrong-level-timer-display.patch
0091-Fix-the-visual-placement-of-the-fake_exit-trap.patch
0092-Fix-editor-keeps-playing-level-music-after-testing.patch
0093-Fix-levelset-loading-from-the-command-line.patch
0094-Fix-crashes-with-no-actions-available-in-a-level.patch
0095-Fix-the-stretch-x-state-display-in-the-editor.patch
0096-Fix-not-all-snow-particles-used-in-animation.patch
0097-Fix-negative-time-left-shown-on-result-screen.patch
0098-Fix-typo-in-halloween2011-level-The-Ones.patch
0099-Fix-typo-in-xmas2011-level-Spiraling-Away.patch
0100-Fix-typo-in-xmas2011-level-Ice-Block-Blockage.patch
0101-Fix-typo-in-some-language-files.patch
0103-Set-user-level-directory-as-default-in-file-dialog.patch
0104-Add-spawn-at-mouse-position-for-developer-mode.patch
0105-Add-X-Y-editing-capabilities-for-objects-in-editor.patch
0106-Update-shown-properties-in-editor-for-moved-object.patch
0107-Set-and-display-level-time-in-editor-in-seconds.patch
0108-Update-nix-install-instructions.patch
0110-Replaced-grumbel-gmx.de-with-grumbel-gmail.com.patch
0111-Added-missing-string-include.patch
0112-Corrected-shared_ptr-handling.patch
0114-Update-SConscript-to-python3.patch
0115-Replace-sdl-config-with-pkg-config-in-SConscript.patch
0116-Fix-boost-signals2-check.patch
0117-Add-build-options-for-tests-and-extra.patch
0118-Fix-scons-platform-check-to-work-in-Python3.patch
0122-Add-PROJECT_NAME-to-Makefile.patch
0128-Fix-missing-include.patch

pingus-boost_system-is-obsolete.patch
pingus-workaround-sdl-detection.patch
pingus-compilefixes.patch

%description
Pingus is a free Lemmings clone covered under the GPL. Pingus uses SDL,
which should make it portable over a lot of operating systems in the future. At
the moment the main target is Linux. It is possible to play Pingus in a X
window or in fullscreen.

%prep
%autosetup -p1
cd external
rmdir logmich
tar xf %{S:1}
mv logmich-* logmich
rmdir tinygettext
tar xf %{S:2}
mv tinygettext-* tinygettext

%build
%scons \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
%if %{build_extra_input}
	with_xinput=true \
	with_wiimote=true \
%endif
	prefix=%{_prefix} \
	execprefix=%{_bindir} \
	datadir=%{_gamesdatadir} \
	libdir=%{_libdir} \
	libexecdir=%{_libexecdir}

%install
%make_install \
	PREFIX=%{_prefix} \
	DATADIR=%{_gamesdatadir}/%{name} \
	MANDIR=%{_mandir} \
	BINDIR=%{_bindir} \
	LIBDIR=%{_libdir}


install -m 755 -d %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Pingus
Comment=A free Lemmings clone
Exec=%{_bindir}/%{name}
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

%files
%doc AUTHORS COPYING README*
%{_bindir}/pingus
%{_libexecdir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man1/pingus.6*
