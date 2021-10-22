%define		sha256 3a34109f55ce0f483a1b18cc0c2814825a2fec67a56eff591a07759ba5e18eca

Name:		tl-legacy
Version:	130.0
Release:	1
Summary:	Unofficial Minecraft launcher
License:	Custom
Source0:	https://tlauncherrepo.com/legacy/bootstrap/%{sha256}.jar
Source1:	tl-logo.png
Source2:	tl-legacy.desktop
Source3:	tl-legacy

Requires:	jre-openjdk
Requires:	jre-headless
Requires:	libdrm
Requires:	fontconfig
Requires:	xrandr
Requires:	cairo
Requires:	pango
Requires:	xdg-utils
Requires:	bash

BuildRequires:	ImageMagick

Recommends:	gtk3

BuildArch:	noarch

%description
Unofficial Minecraft: Java Edition launcher

%build
mkdir -p %{_builddir}/tmp
cp %{SOURCE1} %{_builddir}/tmp/tl.png
for size in 512x512 256x256 192x192 128x128 96x96 48x48; do
  convert -verbose -resize ${size} -quality 100 %{_builddir}/tmp/tl.png \
                                                %{_builddir}/tmp/${size}.png
done

%install
install -D -m 755 %{SOURCE0} %{buildroot}/opt/%{name}/%{name}.jar
for size in 512x512 256x256 192x192 128x128 96x96 48x48; do
  install -D -m 644 %{_builddir}/tmp/${size}.png \
                    %{buildroot}/%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done
install -D -m 644 %{SOURCE2} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -D -m 755 %{SOURCE3} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
/opt/%{name}
/opt/%{name}/%{name}.jar
