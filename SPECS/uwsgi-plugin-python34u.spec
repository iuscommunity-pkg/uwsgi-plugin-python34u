%global python python34u
%global uwsgi uwsgi
%global srcname uwsgi

Name: %{uwsgi}-plugin-%{python}
Version: 2.0.12
Release: 1.ius%{?dist}
Summary: uWSGI - Plugin for Python 3.4 support
Group: System Environment/Daemons
License: GPLv2 with exceptions
URL: https://github.com/unbit/%{srcname}
Source0: http://projects.unbit.it/downloads/%{srcname}-%{version}.tar.gz
BuildRequires: %{python}-devel
Requires: %{python}
Requires: %{uwsgi}-plugin-common


%description
This package contains the Python 3.4 plugin for uWSGI


%prep
%setup -q -n %{srcname}-%{version}


%build
# modeled after extensions in the main Fedora/EPEL uwsgi spec file
CFLAGS="%{optflags} -Wno-unused-but-set-variable" %{__python3} uwsgiconfig.py --plugin plugins/python pyonly %{python}


%install
%{__install} -Dpm0755 %{python}_plugin.so %{buildroot}%{_libdir}/%{uwsgi}/%{python}_plugin.so


%files
%{_libdir}/%{uwsgi}/%{python}_plugin.so


%changelog
* Thu Jun 30 2016 Carl George <carl.george@rackspace.com> - 2.0.12-1.ius
- Update to match current EPEL version

* Wed Jun 17 2015 Carl George <carl.george@rackspace.com> - 2.0.9-1.ius
- Initial package
