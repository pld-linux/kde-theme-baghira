
%define		_name	baghira
%define		_name_ver	0.3q

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	%{_name_ver}
Release:	2
License:	Not specified
Group:		Themes
Source0:	http://dl.sourceforge.net/baghira/%{_name}-0.3q.tar.bz2
# Source0-md5:	5ce2db262f061f6fbb0c026bf2c77d82
Source1:	http://dl.sourceforge.net/baghira/%{_name}-deco-0.4-pre4.tar.bz2
# Source1-md5:	7bf8cfb50c85535b120238f23b514f2a
Patch0:		%{name}-gcc34fix.patch
URL:		http://www.kde-look.org/content/show.php?content=8692
# Also:	http://www.kde-look.org/content/show.php?content=11149
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
#BuildRequires:	unsermake
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} KDE theme.

%description -l pl
Motyw KDE %{_name}.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
%{_name} is a slicker style that was designed to look nice with
slicker. To developer's surprise, this style looks good even without
slicker.

%description -n kde-style-%{_name} -l pl
%{_name} to styl stworzony by wspó³gra³ z aplikacj± slicker. Ku
zaskoczeniu twórców, styl ten jednak okaza³ siê piêknie wygl±daæ nawet
bez slickera.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl):	Motyw ikon do kde - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
%{_name} is an icon them.

%description -n kde-icons-%{_name} -l pl
%{_name} to motyw ikon.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
Color scheme for KDE style - %{_name}

%description -n kde-colorscheme-%{_name} -l pl
Schemat kolorów do stylu KDE - %{_name}

%package -n kde-wallpaper-%{_name}
Summary:	KDE wallpaper - %{_name}
Summary(pl):	Tapeta do KDE - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdelibs

%description -n kde-wallpaper-%{_name}
A wallpaper to go with KDE %{_name} theme.

%description -n kde-wallpaper-%{_name} -l pl
Tapeta pasuj±ca do motywu %{_name}.

%package -n kdm-user-pictures-%{_name}
Summary:	KDM user picture - %{_name}
Summary(pl):	Obrazki dla u¿ytkowników w KDM - %{_name}
Group:		Themes
# Contains /usr/share/wallpapers
Requires:	kdm

%description -n kdm-user-pictures-%{_name}
KDM user picture - %{_name}.

%description -n kdm-user-pictures-%{_name} -lpl
Obrazki dla u¿ytkowników w KDM - %{_name}.

%package -n kde-splashplugin-%{_name}
Summary:	ksplash plugin %{_name}
Summary(pl):	Wtyczka ksplash %{_name}
Group:		X11/Amusements
Requires:	kdebase-desktop

%description -n kde-splashplugin-%{_name}
ksplash plugin %{_name}

%description -n kde-splashplugin-%{_name} -l pl
Wtyczka ksplash %{_name}

%package -n kde-colorscheme-%{_name}-thinkeramik
Summary:	Color scheme for %{_name} theme to go with thinkeramik style
Summary(pl):	Schemat kolorów dla motywu %{_name} pasuj±cy do stylu thinkeramik
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-thinkeramik >= 3.1.4

%description -n kde-colorscheme-%{_name}-thinkeramik
Color scheme for %{_name} theme to go with thinkeramik style.

%description -n kde-colorscheme-%{_name}-thinkeramik -l pl
Schemat kolorów dla motywu %{_name} pasuj±cy do stylu thinkeramik.

%package -n kde-colorscheme-%{_name}-activeheart
Summary:	Color scheme for %{_name} theme to go with activeheart style
Summary(pl):	Schemat kolorów dla motywu %{_name} pasuj±cy do stylu activeheart
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-activeheart >= 1.1.7-2

%description -n kde-colorscheme-%{_name}-activeheart
Color scheme for %{_name} theme to go with thinkeramik style.

%description -n kde-colorscheme-%{_name}-activeheart -l pl
Schemat kolorów dla motywu %{_name} pasuj±cy do stylu thinkeramik.

%package -n kde-splash-%{_name}
Summary:	Splash screen %{_name} theme
Summary(pl):	Obrazek startowy dla motywu %{_name}
Group:		Themes
Requires:	kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
Splash screen %{_name} theme.

%description -n kde-splash-%{_name} -l pl
Obrazek startowy dla motywu %{_name}.

%package -n kde-kside-%{_name}
Summary:	Kicker sidebar from %{_name}
Summary(pl):	Boczny pasek do menu kde z motywu %{_name}
Group:		Themes
Requires:	kdebase-kicker >= 9:3.1.90.030726-2
Provides:	kde-kside
Obsoletes:	kde-kside

%description -n kde-kside-%{_name}
Kicker sidebar from %{_name}.

%description -n kde-kside-%{_name} -l pl
Boczny pasek do menu kde z motywu %{_name}.

%package -n kopete-emoticons-%{_name}
Summary:	Kopete emoticons from %{_name} theme
Summary(pl):	Emotikony do kopete z tematu %{_name}
Group:		Themes
Requires:	kdenetwork-kopete

%description -n kopete-emoticons-%{_name}
Kopete emoticons from %{_name} theme.

%description -n kopete-emoticons-%{_name} -l pl
Emotikony do kopete z tematu %{_name}.


%package -n kde-decoration-icewm-%{_name}
Summary:	Icewm window decoration for kwin - %{_name}
Summary(pl):	Dekoracja icewm dla kwin - %{_name}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
Icewm window decoration for kwin - %{_name}.

%description -n kde-decoration-icewm-%{_name} -l pl
Dekoracja icewm dla kwin - %{_name}.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl):	Dekoracja kwin - %{_name}
Group:		Themes
Requires:	kdebase-desktop-libs

%description -n kde-decoration-%{_name}
Kwin decoration - %{_name}.

%description -n kde-decoration-%{_name} -l pl
Dekoracja kwin - %{_name}.

%prep
%setup -q -n %{_name}-%{version} -a1
%patch0 -p1

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp -f /usr/share/automake/config.sub admin
##export UNSERMAKE=/usr/share/unsermake/unsermake
##%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

cd %{_name}-deco-0.4-pre4
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd %{_name}-deco-0.4-pre4
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
install *.kcsrc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
cd -

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Settings/LookNFeel,%{_desktopdir}/kde}/kcmbaghira.desktop
echo "Categories=Qt;KDE;X-KDE-settings-looknfeel;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kcmbaghira.desktop
echo "OnlyShowIn=KDE;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kcmbaghira.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kcm_*.la
%attr(755,root,root) %{_libdir}/kde3/kcm_*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc
%{_desktopdir}/kde/kcmbaghira.desktop

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc
