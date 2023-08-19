%define target avr

Name:           %{target}-gdb
Version:        13.2
Release:        1%{?dist}
Summary:        GDB for (remote) debugging %{target} binaries
License:        GPLv3+ and GPLv3+ with exceptions and GPLv2+ and GPLv2+ with exceptions and GPL+ and LGPLv2+ and LGPLv3+ and BSD and Public Domain and GFDL
URL:            http://www.sourceware.org/gdb/

%global tarname gdb-%{version}

Source:         https://sourceware.org/pub/gdb/releases/%{tarname}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
BuildRequires:  texinfo
BuildRequires:  make gmp-devel expat-devel xz-devel guile-devel mpfr-devel python-devel zlib-devel

Requires: expat xz guile mpfr python zlib

Provides: bundled(libiberty)

%description
This is a special version of GDB, the GNU Project debugger, for (remote)
debugging %{target} binaries. GDB allows you to see what is going on
inside another program while it executes or what another program was doing at
the moment it crashed. 


%prep
%setup -q -c


%build
mkdir -p build
pushd build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" \
  ../gdb-%{version}/configure --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --target=%{target} --disable-werror \
  --disable-rpath \
  --with-system-zlib
make %{?_smp_mflags}
popd


%install
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd

# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_datadir}/gdb
# Should not be installed
rm    $RPM_BUILD_ROOT%{_libdir}/libavr-sim.a

# no need for devel files
rm -rf $RPM_BUILD_ROOT%{_includedir}

# Clashes with other packages
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/

%files
%doc gdb-%{version}/COPYING* gdb-%{version}/README*
%{_bindir}/%{name}*
%{_bindir}/avr-run
%{_mandir}/man1/avr-*
%{_mandir}/man5/avr-*


%changelog
* Sat Aug 19 2023 Johannes Pfau <johannespfau@gmail.com> - 13.2-1
- move to latest upstream release

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 29 2018 Gianluca Sforna <giallu@gmail.com> - 8.1-1
- move to latest upstream release

* Tue Jun 26 2018 Gianluca Sforna <giallu@gmail.com> - 7.1-18
- Fix FTBS #1555621

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 7.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Jaromir Capik <jcapik@redhat.com> - 7.1-8
- Fixing aarch64 build (#925064)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 15 2012 Jon Ciesla <limburgher@gmail.com> - 7.1-6
- Provides: bundled(libiberty)

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 27 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 7.1-3
- Pass --disable-werror to configure (Fix FTBS BZ#716110).
- Remove hacks to work-around -Werror.
- Get rid of superflous calls to "chrpath".
- Remove BR: chrpath.
- Remove %%{_libdir}/libavr-sim.a.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 11 2010 Thibault North <tnorth@fedoraproject.org> - 7.1-1
- avr-gdb 7.1

* Tue Mar 16 2010 Thibault North <tnorth@fedoraproject.org> - 7.0.1-2
- Also apply chrpath to avr-run

* Tue Mar 16 2010 Thibault North <tnorth@fedoraproject.org> - 7.0.1-1
- New upstream release
- Remove now obsolete patches

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 6.6-11
- Use bzipped upstream tarball.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Apr  2 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 6.6-8
- Fix missing prototype compiler warnings

* Mon Feb 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 6.6-7
- Rebuild again as koji successfully build it but didn't tag it

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 6.6-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 6.6-5
- Update License tag for new Licensing Guidelines compliance
- Fix building with new glibc open checking

* Thu Jun 14 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 6.6-4
- Add BuildRequires: ncurses-devel (bz 243248)
- Use VPATh building (bz 243248)

* Mon Jun 11 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 6.6-3
- Remove bogus avr-gcc-c++ Requires (bz 243248)

* Fri Jun  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 6.6-2
- Various specfile cleanups

* Thu May 31 2007 Lennart Kneppers <lennartkneppers@gmail.com> 6.6-1
- Initial release
