#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : connections
Version  : 41.0
Release  : 1
URL      : https://gitlab.gnome.org/GNOME/connections/-/archive/41.0/connections-41.0.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/connections/-/archive/41.0/connections-41.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: connections-bin = %{version}-%{release}
Requires: connections-data = %{version}-%{release}
Requires: connections-license = %{version}-%{release}
Requires: connections-locales = %{version}-%{release}
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gtk-frdp
BuildRequires : gtk-frdp-dev
BuildRequires : pkgconfig(gtk-frdp-0.1)
BuildRequires : pkgconfig(gtk-vnc-2.0)
BuildRequires : pkgconfig(libhandy-1)
Patch1: buildfail.patch

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
%setup -q -n connections-41.0
cd %{_builddir}/connections-41.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1632331556
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/connections
cp %{_builddir}/connections-41.0/COPYING %{buildroot}/usr/share/package-licenses/connections/4aafa844fab55582342f86019d5710e5fa0cde75
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-connections

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/help/hu/gnome-connections/connect.page
/usr/share/help/hu/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/hu/gnome-connections/index.page
/usr/share/help/hu/gnome-connections/legal.xml
/usr/share/help/id/gnome-connections/connect.page
/usr/share/help/id/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/id/gnome-connections/index.page
/usr/share/help/id/gnome-connections/legal.xml
/usr/share/help/pl/gnome-connections/connect.page
/usr/share/help/pl/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/pl/gnome-connections/index.page
/usr/share/help/pl/gnome-connections/legal.xml
/usr/share/help/pt_BR/gnome-connections/connect.page
/usr/share/help/pt_BR/gnome-connections/figures/org.gnome.Connections.svg
/usr/share/help/pt_BR/gnome-connections/index.page
/usr/share/help/pt_BR/gnome-connections/legal.xml
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/connections/4aafa844fab55582342f86019d5710e5fa0cde75

%files locales -f gnome-connections.lang
%defattr(-,root,root,-)

