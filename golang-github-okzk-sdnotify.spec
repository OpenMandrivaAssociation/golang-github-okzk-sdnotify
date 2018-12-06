# Run tests in check section
%bcond_without check

%global goipath         github.com/okzk/sdnotify
%global commit          d9becc38acbd785892af7637319e2c5e101057f7

%global common_description %{expand:
sd_notify utility for golang.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        sd_notify utility for golang
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Sat Oct 06 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20181006gitd9becc3
- Bump to commit d9becc38acbd785892af7637319e2c5e101057f7

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gited8ca10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Mar 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180422gited8ca10
- First package for Fedora

