# IUS spec file for uwsgi-plugin-python34u
#
# This package is intended to work with uwsgi from EPEL and python34u from IUS.
# It should remain at the same version as the EPEL uwsgi package to ensure
# compatibility.

%global python python34u

Name: uwsgi-plugin-%{python}
Version: 2.0.13.1
Release: 1.ius%{?dist}
Summary: uWSGI - Plugin for Python support
Group: System Environment/Daemons
License: GPLv2 with exceptions
URL: https://github.com/unbit/uwsgi
BuildRequires: uwsgi-devel = %{version}
BuildRequires: %{python}-devel
BuildRequires: libuuid-devel
BuildRequires: pcre-devel
BuildRequires: openssl-devel
BuildRequires: libcap-devel
Requires: uwsgi-plugin-common = %{version}
Requires: %{python}

%{?filter_provides_in: %filter_provides_in %{_libdir}/uwsgi/.*\.so$}
%{?filter_setup}


%description
This package contains the python plugin for uWSGI.  Designed to work with the
uwsgi packages in EPEL, but built against %{python} from IUS.


%prep
%setup -q -c -T


%build
export CFLAGS="%{optflags} -Wno-unused-but-set-variable"
export PYTHON=%{__python3}
uwsgi --build-plugin "%{_usrsrc}/uwsgi/%{version}/plugins/python %{python}"


%install
%{__install} -Dpm0755 %{python}_plugin.so %{buildroot}%{_libdir}/uwsgi/%{python}_plugin.so


%files
%{_libdir}/uwsgi/%{python}_plugin.so


%changelog
* Thu Sep 15 2016 Carl George <carl.george@rackspace.com> - 2.0.13.1-1.ius
- Latest upstream

* Thu Jun 30 2016 Carl George <carl.george@rackspace.com> - 2.0.12-1.ius
- Update to match current EPEL version
- Clarify this package is intended to work with uwsgi from EPEL
- Use uwsgi-devel sources instead of duplicate source tarball
- Filter auto-provides
- Add missing build requirements

* Wed Jun 17 2015 Carl George <carl.george@rackspace.com> - 2.0.9-1.ius
- Initial package
