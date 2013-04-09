Summary:	Simple database library for storing time-series data
Name:		python-whisper
Version:	0.9.10
Release:	1
License:	Apache v2.0
Group:		Development/Libraries
Source0:	https://github.com/downloads/graphite-project/whisper/whisper-%{version}.tar.gz
# Source0-md5:	cf7d7d73e115f50e682f46c4eb52be09
URL:		https://launchpad.net/graphite/
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
simple database library for storing time-series data (similar in
design to RRD)

%prep
%setup -q -n whisper-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

# Temp mv to non .py locations
cd $RPM_BUILD_ROOT%{_bindir}
%{__mv} rrd2whisper.py rrd2whisper
%{__mv} whisper-create.py whisper-create
%{__mv} whisper-dump.py whisper-dump
%{__mv} whisper-fetch.py whisper-fetch
%{__mv} whisper-info.py whisper-info
%{__mv} whisper-merge.py whisper-merge
%{__mv} whisper-resize.py whisper-resize
%{__mv} whisper-set-aggregation-method.py whisper-set-aggregation-method
%{__mv} whisper-update.py whisper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rrd2whisper
%attr(755,root,root) %{_bindir}/whisper-create
%attr(755,root,root) %{_bindir}/whisper-dump
%attr(755,root,root) %{_bindir}/whisper-fetch
%attr(755,root,root) %{_bindir}/whisper-info
%attr(755,root,root) %{_bindir}/whisper-merge
%attr(755,root,root) %{_bindir}/whisper-resize
%attr(755,root,root) %{_bindir}/whisper-set-aggregation-method
%attr(755,root,root) %{_bindir}/whisper-update
%{py_sitescriptdir}/whisper-%{version}-py*.egg-info
%{py_sitescriptdir}/whisper.py[co]
