#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : olefile
Version  : 0.46
Release  : 32
URL      : https://files.pythonhosted.org/packages/34/81/e1ac43c6b45b4c5f8d9352396a14144bba52c8fec72a80f425f6a4d653ad/olefile-0.46.zip
Source0  : https://files.pythonhosted.org/packages/34/81/e1ac43c6b45b4c5f8d9352396a14144bba52c8fec72a80f425f6a4d653ad/olefile-0.46.zip
Summary  : Python package to parse, read and write Microsoft OLE2 files (Structured Storage or Compound Document, Microsoft Office)
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: olefile-license = %{version}-%{release}
Requires: olefile-python = %{version}-%{release}
Requires: olefile-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=======
        
        |Build Status TravisCI| |Build Status AppVeyor| |Coverage Status|
        |Documentation Status| |PyPI| |Can I Use Python 3?| |Say Thanks!|

%package license
Summary: license components for the olefile package.
Group: Default

%description license
license components for the olefile package.


%package python
Summary: python components for the olefile package.
Group: Default
Requires: olefile-python3 = %{version}-%{release}

%description python
python components for the olefile package.


%package python3
Summary: python3 components for the olefile package.
Group: Default
Requires: python3-core
Provides: pypi(olefile)

%description python3
python3 components for the olefile package.


%prep
%setup -q -n olefile-0.46
cd %{_builddir}/olefile-0.46

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603397304
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/olefile
cp %{_builddir}/olefile-0.46/LICENSE.txt %{buildroot}/usr/share/package-licenses/olefile/39139a785b98452f34e53f1dd9916f6a6d0a8ebf
cp %{_builddir}/olefile-0.46/doc/License.rst %{buildroot}/usr/share/package-licenses/olefile/b26f237ee1e7c24a2f98969fee5228ce94b4d8b7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/olefile/39139a785b98452f34e53f1dd9916f6a6d0a8ebf
/usr/share/package-licenses/olefile/b26f237ee1e7c24a2f98969fee5228ce94b4d8b7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
