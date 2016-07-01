# IUS spec file for uwsgi-plugin-python34u
#
# This package is intended to work with uwsgi from EPEL and python34u from IUS.
# It should remain at the same version as the EPEL uwsgi package to ensure
# compatibility.

%global python python34u
%global srcname uwsgi

Name: uwsgi-plugin-%{python}
Version: 2.0.12
Release: 1.ius%{?dist}
Summary: uWSGI - Plugin for Python support
Group: System Environment/Daemons
License: GPLv2 with exceptions
URL: https://github.com/unbit/%{srcname}
Source0: http://projects.unbit.it/downloads/%{srcname}-%{version}.tar.gz
BuildRequires: %{python}-devel
Requires: %{python}
Requires: uwsgi-plugin-common


%description
This package contains the python plugin for uWSGI.  Designed to work with the
uwsgi packages in EPEL, but built against %{python} from IUS.


%prep
%setup -q -n %{srcname}-%{version}


%build
# modeled after extensions in the main Fedora/EPEL uwsgi spec file
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3} uwsgiconfig.py --plugin plugins/python pyonly %{python}


%install
%{__install} -Dpm0755 %{python}_plugin.so %{buildroot}%{_libdir}/uwsgi/%{python}_plugin.so


%files
%{_libdir}/uwsgi/%{python}_plugin.so


%changelog
* Thu Jun 30 2016 Carl George <carl.george@rackspace.com> - 2.0.12-1.ius
- Update to match current EPEL version
- Clarify this package is intended to work with uwsgi from EPEL

* Wed Jun 17 2015 Carl George <carl.george@rackspace.com> - 2.0.9-1.ius
- Initial package
