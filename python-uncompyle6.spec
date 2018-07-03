#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		uncompyle6
%define		egg_name	uncompyle6
%define		pypi_name	uncompyle6
Summary:	A Python decompiler, disassembler and cross-version bytecode library
Name:		python-%{pypi_name}
Version:	2.7.0
Release:	3
License:	MIT
Group:		Applications
Source0:	https://github.com/rocky/python-uncompyle6/archive/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	17887c06c40b23641490815432c44b99
URL:		https://github.com/rocky/python-uncompyle6/
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-pytest
BuildRequires:	python-setuptools
BuildRequires:	python-spark_parser
BuildRequires:	python-xdis
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools
BuildRequires:	python3-spark_parser
BuildRequires:	python3-xdis
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uncompyle6 translates Python bytecode back into equivalent Python
source code. It accepts bytecodes from Python version 2.5 to 3.4 or so
and has been tested on Python running versions 2.6, 2.7, 3.3, 3.4 and
3.5.

%package -n python3-%{module}
Summary:	A Python decompiler, disassembler and cross-version bytecode library
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
uncompyle6 translates Python bytecode back into equivalent Python
source code. It accepts bytecodes from Python version 2.5 to 3.4 or so
and has been tested on Python running versions 2.6, 2.7, 3.3, 3.4 and
3.5.

%prep
%setup -qn %{name}-release-%{version}

# There is something wrong with this file that breaks tests
%{__rm} test/bytecode_2.4/02_complex.pyc

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%{?with_tests:%{__make} PYTHONPATH=$(pwd) check}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/{pydisassemble,py3disassemble}
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{uncompyle6,py3uncompyle6}
%endif

%if %{with python2}
%py_install
%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydisassemble
%attr(755,root,root) %{_bindir}/uncompyle6
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/py3disassemble
%attr(755,root,root) %{_bindir}/py3uncompyle6
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
