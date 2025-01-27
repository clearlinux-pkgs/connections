#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : connections
Version  : 47.2.1
Release  : 3
URL      : https://gitlab.gnome.org/GNOME/connections/-/archive/47.2.1/connections-47.2.1.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/connections/-/archive/47.2.1/connections-47.2.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: connections-bin = %{version}-%{release}
Requires: connections-data = %{version}-%{release}
Requires: connections-license = %{version}-%{release}
Requires: connections-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gtk-frdp
BuildRequires : gtk-frdp-dev
BuildRequires : pkgconfig(gtk-vnc-2.0)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(libsecret-1)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Connections
A remote desktop client for the GNOME desktop environment.
<img src="https://gitlab.gnome.org/GNOME/connections/-/raw/master/data/screenshot.png" width="800"/>

%package bin
Summary: bin components for the connections package.
Group: Binaries
Requires: connections-data = %{version}-%{release}
Requires: connections-license = %{version}-%{release}

%description bin
bin components for the connections package.


%package data
Summary: data components for the connections package.
Group: Data

%description data
data components for the connections package.


%package doc
Summary: doc components for the connections package.
Group: Documentation

%description doc
doc components for the connections package.


%package license
Summary: license components for the connections package.
Group: Default

%description license
license components for the connections package.


%package locales
Summary: locales components for the connections package.
Group: Default

%description locales
locales components for the connections package.


%prep
%setup -q -n connections-47.2.1
cd %{_builddir}/connections-47.2.1
pushd ..
cp -a connections-47.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1738011129
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/connections
cp %{_builddir}/connections-%{version}/COPYING %{buildroot}/usr/share/package-licenses/connections/4aafa844fab55582342f86019d5710e5fa0cde75 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-connections
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gnome-connections
/usr/bin/gnome-connections

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Connections.desktop
/usr/share/dbus-1/services/org.gnome.Connections.service
/usr/share/glib-2.0/schemas/org.gnome.Connections.gschema.xml
/usr/share/icons/hicolor/scalable/apps/org.gnome.Connections.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Connections-symbolic.svg
/usr/share/metainfo/org.gnome.Connections.appdata.xml
/usr/share/mime-packages/org.gnome.Connections.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/gnome-connections/connect.page
/usr/share/help/C/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/C/gnome-connections/index.page
/usr/share/help/C/gnome-connections/legal.xml
/usr/share/help/ca/gnome-connections/connect.page
/usr/share/help/ca/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/ca/gnome-connections/index.page
/usr/share/help/ca/gnome-connections/legal.xml
/usr/share/help/cs/gnome-connections/connect.page
/usr/share/help/cs/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/cs/gnome-connections/index.page
/usr/share/help/cs/gnome-connections/legal.xml
/usr/share/help/da/gnome-connections/connect.page
/usr/share/help/da/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/da/gnome-connections/index.page
/usr/share/help/da/gnome-connections/legal.xml
/usr/share/help/de/gnome-connections/connect.page
/usr/share/help/de/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/de/gnome-connections/index.page
/usr/share/help/de/gnome-connections/legal.xml
/usr/share/help/en_GB/gnome-connections/connect.page
/usr/share/help/en_GB/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/en_GB/gnome-connections/index.page
/usr/share/help/en_GB/gnome-connections/legal.xml
/usr/share/help/es/gnome-connections/connect.page
/usr/share/help/es/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/es/gnome-connections/index.page
/usr/share/help/es/gnome-connections/legal.xml
/usr/share/help/eu/gnome-connections/connect.page
/usr/share/help/eu/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/eu/gnome-connections/index.page
/usr/share/help/eu/gnome-connections/legal.xml
/usr/share/help/fr/gnome-connections/connect.page
/usr/share/help/fr/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/fr/gnome-connections/index.page
/usr/share/help/fr/gnome-connections/legal.xml
/usr/share/help/gl/gnome-connections/connect.page
/usr/share/help/gl/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/gl/gnome-connections/index.page
/usr/share/help/gl/gnome-connections/legal.xml
/usr/share/help/hu/gnome-connections/connect.page
/usr/share/help/hu/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/hu/gnome-connections/index.page
/usr/share/help/hu/gnome-connections/legal.xml
/usr/share/help/id/gnome-connections/connect.page
/usr/share/help/id/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/id/gnome-connections/index.page
/usr/share/help/id/gnome-connections/legal.xml
/usr/share/help/ko/gnome-connections/connect.page
/usr/share/help/ko/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/ko/gnome-connections/index.page
/usr/share/help/ko/gnome-connections/legal.xml
/usr/share/help/nl/gnome-connections/connect.page
/usr/share/help/nl/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/nl/gnome-connections/index.page
/usr/share/help/nl/gnome-connections/legal.xml
/usr/share/help/pl/gnome-connections/connect.page
/usr/share/help/pl/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/pl/gnome-connections/index.page
/usr/share/help/pl/gnome-connections/legal.xml
/usr/share/help/pt/gnome-connections/connect.page
/usr/share/help/pt/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/pt/gnome-connections/index.page
/usr/share/help/pt/gnome-connections/legal.xml
/usr/share/help/pt_BR/gnome-connections/connect.page
/usr/share/help/pt_BR/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/pt_BR/gnome-connections/index.page
/usr/share/help/pt_BR/gnome-connections/legal.xml
/usr/share/help/ru/gnome-connections/connect.page
/usr/share/help/ru/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/ru/gnome-connections/index.page
/usr/share/help/ru/gnome-connections/legal.xml
/usr/share/help/sv/gnome-connections/connect.page
/usr/share/help/sv/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/sv/gnome-connections/index.page
/usr/share/help/sv/gnome-connections/legal.xml
/usr/share/help/tr/gnome-connections/connect.page
/usr/share/help/tr/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/tr/gnome-connections/index.page
/usr/share/help/tr/gnome-connections/legal.xml
/usr/share/help/uk/gnome-connections/connect.page
/usr/share/help/uk/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/uk/gnome-connections/index.page
/usr/share/help/uk/gnome-connections/legal.xml
/usr/share/help/zh_CN/gnome-connections/connect.page
/usr/share/help/zh_CN/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/zh_CN/gnome-connections/index.page
/usr/share/help/zh_CN/gnome-connections/legal.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/connections/4aafa844fab55582342f86019d5710e5fa0cde75

%files locales -f gnome-connections.lang
%defattr(-,root,root,-)

