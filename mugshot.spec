Summary:	User profile configuration utility
Summary(pl.UTF-8):	Narzędzie do konfigurowania profilu uyżytkownika
Name:		mugshot
Version:	0.4.3
Release:	1
Epoch:		1
License:	GPL v3
Group:		X11/Applications
Source0:	https://github.com/bluesabre/mugshot/releases/download/%{name}-%{version}/mugshot-%{version}.tar.gz
# Source0-md5:	1c504dcec181159ff5aa896bed9605ab
# Disabling webcam source of avatar, as it can be unstable
Patch0:		disable_webcam.patch
URL:		https://github.com/bluesabre/mugshot
BuildRequires:	gobject-introspection
BuildRequires:	intltool
BuildRequires:	python3-devel
BuildRequires:	python3-distutils-extra
BuildRequires:	python3-pexpect
BuildRequires:	python3-pycairo-devel
BuildRequires:	python3-pygobject3-devel
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	tar >= 1:1.22
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	hicolor-icon-theme
Requires:	python3
Requires:	python3-dbus
Requires:	python3-pexpect
Requires:	python3-pycairo
Requires:	python3-pygobject3
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mugshot is a user configuration utility that allows updating personal
user details and avatar.

%description -l pl.UTF-8
Mugshot to narzędzie do konfiguracji profilu użytkownika pozwalające
pozwalające zmieniać dane osobiste i avatar.

%prep
%setup -q
%patch -P 0 -p1

%build
%{__python3} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py install \
	--prefix=%{_prefix} \
	--install-purelib=%{py3_sitescriptdir} \
	--install-platlib=%{py3_sitedir} \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

# Remove unused doc directory
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

# unsupported locale
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ms@Arab

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%update_desktop_database_post
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.md NEWS
%attr(755,root,root) %{_bindir}/mugshot
%{_desktopdir}/org.bluesabre.Mugshot.desktop
%{_datadir}/glib-2.0/schemas/org.bluesabre.mugshot.gschema.xml
%{_iconsdir}/hicolor/16x16/apps/mugshot.svg
%{_iconsdir}/hicolor/22x22/apps/mugshot.svg
%{_iconsdir}/hicolor/24x24/apps/mugshot.svg
%{_iconsdir}/hicolor/48x48/apps/mugshot.svg
%{_iconsdir}/hicolor/64x64/apps/mugshot.svg
%{_iconsdir}/hicolor/scalable/apps/mugshot.svg
%{_mandir}/man1/mugshot.1*
%{_datadir}/metainfo/mugshot.appdata.xml
%{_datadir}/mugshot
%{py3_sitescriptdir}/%{name}-%{version}-*-info
%{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/%{name}_lib
