%global commit0 bd061dbe34349e052d6affc2d52687e40f1ee0ef
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global service tripleo-puppet-elements

%{!?upstream_version: %global upstream_version %{version}}

# Turn off the brp-python-bytecompile script
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')

Name:		openstack-tripleo-puppet-elements
Summary:	OpenStack TripleO Puppet Elements for diskimage-builder
Version:    0.0.2
Release:    1%{?dist}
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
# Once we have stable branches and stable releases we can go back to using release tarballs
Source0:  https://github.com/openstack/%{service}/archive/%{commit0}.tar.gz#/%{service}-%{shortcommit0}.tar.gz

BuildArch:	noarch
BuildRequires:  git
BuildRequires:	python
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

%description
OpenStack TripleO Puppet Elements is a collection of elements for
diskimage-builder that can be used to build OpenStack images configured with
Puppet for the TripleO program.

%prep
%autosetup -n %{service}-%{commit0} -S git

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root=%{buildroot}

# remove .git-keep-empty files that get installed
find %{buildroot} -name .git-keep-empty | xargs rm -f

%files
%doc LICENSE
%doc README.md
%{python_sitelib}/tripleo_puppet_elements*
%{_datadir}/tripleo-puppet-elements

%changelog
* Mon Oct 19 2015 John Trowbridge <trown@redhat.com> - 0.0.11-1
- Use a source tarball for a git hash that has passed delorean CI for liberty release

* Wed Feb 25 2014 James Slagle <jslagle@redhat.com> 0.0.1-1
- Initial packaging
