Summary:	Python byte-code to source-code converter
Name:		uncompyle2
Version:	1.1
Release:	1
License:	GPL v3
Group:		Applications
Source0:	https://github.com/wibiti/uncompyle2/archive/dffbdc4/%{name}-%{version}.tar.gz
# Source0-md5:	1875d3d9b00ee0b08c845a16795e19ad
URL:		https://github.com/wibiti/uncompyle2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'uncompyle2' converts Python byte-code back into equivalent Python
source. It accepts byte-code from Python version 2.7 only.
Additionally, it will only run on Python 2.7.

%prep
%setup -qc
mv %{name}-*/* .

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/uncompyle2
%{py_sitescriptdir}/uncompyle2
%{py_sitescriptdir}/uncompyle2-%{version}-py*.egg-info
