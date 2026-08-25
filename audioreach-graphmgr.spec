%global debug_package %{nil}

Name:           audioreach-graphmgr
Version:        1.0.1
Release:        1%{?dist}
Summary:        AudioReach Audio Graph Manager libraries
License:        BSD-3-Clause-Clear
URL:            https://github.com/AudioReach/audioreach-graphmgr
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

ExclusiveArch:  aarch64

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  expat-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(spf)
BuildRequires:  pkgconfig(kvh2xml)
BuildRequires:  pkgconfig(tinyalsa)

%description
AudioReach Audio Graph Manager (AGM) for Qualcomm platforms.
Manages audio sessions, devices, and metadata for the AudioReach
framework. Provides AGM service library, sound card parser, and
tinyalsa PCM/mixer plugins.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Headers and pkg-config files for building applications that use
the AudioReach Graph Manager libraries.

%prep
%autosetup -n %{name}-%{version}

%build
autoreconf -fi
%configure \
    --with-glib \
    --with-syslog \
    --with-no-ipc

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/backend_conf.xml
%{_libdir}/libagm.so*
%{_libdir}/libsndcardparser.so*
%{_libdir}/libagm_pcm_plugin.so*
%{_libdir}/libagm_mixer_plugin.so*
%{_libdir}/libagmmixer.so*
%{_bindir}/agmplay
%{_bindir}/agmcap

%files devel
%{_includedir}/agm/
%{_includedir}/sndparser/
%{_libdir}/pkgconfig/agm.pc
%{_libdir}/pkgconfig/sndparser.pc
%{_libdir}/pkgconfig/agmplugin.pc
%{_libdir}/pkgconfig/agmtest.pc
%{_libdir}/pkgconfig/agmalsaplugin.pc

%changelog
* Fri Aug 14 2026 Qualcomm Linux <quic_linux@quicinc.com> - 1.0.1-1
- Initial RPM packaging of audioreach-graphmgr version 1.0.1
