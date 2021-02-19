#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : requests-unixsocket
Version  : 0.2.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/4d/ce/78b651fe0adbd4227578fa432d1bde03b4f4945a70c81e252a2b6a2d895f/requests-unixsocket-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/ce/78b651fe0adbd4227578fa432d1bde03b4f4945a70c81e252a2b6a2d895f/requests-unixsocket-0.2.0.tar.gz
Summary  : Use requests to talk HTTP via a UNIX domain socket
Group    : Development/Tools
License  : Apache-2.0
Requires: requests-unixsocket-license = %{version}-%{release}
Requires: requests-unixsocket-python = %{version}-%{release}
Requires: requests-unixsocket-python3 = %{version}-%{release}
Requires: requests
Requires: urllib3
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : requests
BuildRequires : urllib3
BuildRequires : waitress-python

%description
===================

%package license
Summary: license components for the requests-unixsocket package.
Group: Default

%description license
license components for the requests-unixsocket package.


%package python
Summary: python components for the requests-unixsocket package.
Group: Default
Requires: requests-unixsocket-python3 = %{version}-%{release}

%description python
python components for the requests-unixsocket package.


%package python3
Summary: python3 components for the requests-unixsocket package.
Group: Default
Requires: python3-core
Provides: pypi(requests_unixsocket)
Requires: pypi(requests)
Requires: pypi(urllib3)

%description python3
python3 components for the requests-unixsocket package.


%prep
%setup -q -n requests-unixsocket-0.2.0
cd %{_builddir}/requests-unixsocket-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1608052162
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/requests-unixsocket
cp %{_builddir}/requests-unixsocket-0.2.0/LICENSE %{buildroot}/usr/share/package-licenses/requests-unixsocket/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/requests-unixsocket/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
