Name: bloom
Version: 0.12.3
Release: 1
Summary: Debugger for AVR-based embedded systems
License: LGPL-3.0
Url: https://bloom.oscillate.io
Group: Development/Debuggers
Source: https://github.com/bloombloombloom/Bloom/archive/refs/tags/v%{version}.tar.gz
Patch0: bloom_build_fix.patch

AutoReqProv: OFF

BuildRequires:  cmake
BuildRequires:  gcc gcc-c++
BuildRequires:  libusb1-devel
BuildRequires:  hidapi-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  procps-ng-devel
BuildRequires:  php-cli php-xml
BuildRequires:  cmake(Qt6Core) cmake(Qt6Svg) cmake(Qt6UiTools)

Requires:  libusb1
Requires:  hidapi
Requires:  yaml-cpp
Requires:  procps-ng
Requires:  qt6-qtbase qt6-qtsvg qt6-qttools

%description
Debugger for AVR-based embedded systems

%prep
%setup -q -n Bloom-%{version}
%patch -P0 -p1

%build
# Build generates some warnings
# export CXXFLAGS="$CXXFLAGS -Wno-error -Wall"
%cmake . -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/usr/share
mv %{buildroot}/usr/resources %{buildroot}/usr/share/bloom
# Fix paths in the mapping file
sed -i 's|..\\/resources\\/|..\\/share\\/bloom\\/|' %{buildroot}/usr/share/bloom/TargetDescriptionFiles/AVR/Mapping.json

%files
%dir "/usr/share/bloom"
"/usr/share/bloom/*"
"/usr/bin/bloom"
"/usr/lib/udev/rules.d/99-bloom.rules"

%changelog
* Sat Aug 19 2023 Johannes Pfau <johannespfau@gmail.com> - 0.12.3-1
- Initial package build
