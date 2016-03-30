# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global sname tripleo-puppet-elements

Name:           openstack-tripleo-puppet-elements
Summary:        OpenStack TripleO Puppet Elements for diskimage-builder
Version:        XXX
Release:        XXX
License:        ASL 2.0
URL:            https://wiki.openstack.org/wiki/TripleO
Source0:        https://github.com/openstack/%{sname}/archive/%{version}.tar.gz#/%{sname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-d2to1
BuildRequires:  python-pbr
BuildRequires:  git

%description
OpenStack TripleO Puppet Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images configured with
Puppet for the TripleO program.

%prep
%autosetup -S git -n %{sname}-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%doc LICENSE
%doc README.md
%{python2_sitelib}/tripleo_puppet_elements*
%{_datadir}/tripleo-puppet-elements

%changelog
