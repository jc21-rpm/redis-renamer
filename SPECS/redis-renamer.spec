%define debug_package %{nil}

%global gh_user jc21

Name:           redis-renamer
Version:        1.0.0
Release:        1%{?dist}
Summary:        Takes the keys from one Redis server/db and transfer them to another server/db 
Group:          Applications/System
License:        MIT
URL:            https://github.com/%{gh_user}/%{name}
Source:         https://github.com/%{gh_user}/%{name}/archive/v%{version}.tar.gz
BuildRequires:  git golang

%description
Redis Renamer will simply rename the matching keys with a given prefix.

%prep
%setup -qn %{name}-%{version}

%build
go build -v -ldflags="-X main.version=%{version}" -o bin/%{name} cmd/%{name}/main.go

%install
install -Dm0755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Tue Feb 23 2021 Jamie Curnow <jc@jc21.com> 1.0.0-1
- https://github.com/jc21/redis-renamer/releases/tag/v1.0.0

