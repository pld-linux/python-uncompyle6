#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define 	module		uncompyle6
%define 	egg_name	uncompyle6
%define		pypi_name	uncompyle6
Summary:	A Python decompiler, disassembler and cross-version bytecode library
Name:		python-%{pypi_name}
Version:	2.4.0
Release:	1
License:	MIT
Group:		Applications
Source0:	https://github.com/rocky/python-uncompyle6/archive/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	056bdea13e4159fc9283d43d3dc3743c
URL:		https://github.com/rocky/python-uncompyle6/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uncompyle6 translates Python bytecode back into equivalent Python
source code. It accepts bytecodes from Python version 2.5 to 3.4 or so
and has been tested on Python running versions 2.6, 2.7, 3.3, 3.4 and
3.5.

%prep
%setup -qn %{name}-release-%{version}

%build
%py_build

%if %{with tests}
%{__make} PYTHONPATH=$(pwd) check
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pydisassemble
%attr(755,root,root) %{_bindir}/uncompyle6
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
