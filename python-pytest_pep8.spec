# Created by pyp2rpm-2.0.0
%global pypi_name pytest-pep8
%global with_python2 1
%define version 1.0.6

Name:           python-%{pypi_name}
Version:        %{version}
Release:        1
Group:          Development/Python
Summary:        pep8 is a tool to check your Python code against some of the style conventions in PEP 8.

License:        MIT
URL:            https://bitbucket.org/pytest-dev/pytest-pep8
Source0:        https://files.pythonhosted.org/packages/1f/1c/c834344ef39381558b047bea1e3005197fa8457c199d58219996ca07defb/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python-setuptools
 
%if %{with_python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # if with_python2


%description
 py.test plugin for efficiently checking PEP8 compliance every file ending in .py 
 will be discovered and pep8-checked, starting from the command line arguments.

%if %{with_python2}
%package -n     python2-%{pypi_name}
Summary:        pep8 is a tool to check your Python code against some of the style conventions in PEP 8.

%description -n python2-%{pypi_name}
 py.test plugin for efficiently checking PEP8 compliance every file ending in .py 
 will be discovered and pep8-checked, starting from the command line arguments.
%endif # with_python2


%prep
%setup -q -n %{pypi_name}-%{version}

%if %{with_python2}
rm -rf %{py2dir}
cp -a . %{py2dir}
find %{py2dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%endif # with_python2


%build
%{__python} setup.py build

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py build
popd
%endif # with_python2


%install

%if %{with_python2}
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python2

%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc  README.txt LICENSE CHANGELOG
%{python_sitelib}/*/*
%{python_sitelib}/pytest_pep8.py


%if %{with_python2}
%files -n python2-%{pypi_name}
%doc  README.txt LICENSE CHANGELOG
%{python2_sitelib}/*/*
%{python2_sitelib}/pytest_pep8.*
%endif # with_python2

