# TODO:
# - bootsplash

%define		_name	baghira
%define		_name_ver	0.8

Summary:	KDE theme - %{_name}
Summary(pl.UTF-8):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	%{_name_ver}
Release:	2
License:	GPL v2
Group:		Themes
Source0:	http://dl.sourceforge.net/baghira/%{_name}-%{_name_ver}.tar.bz2
# Source0-md5:	d76e04020c628ba5de69d066a66221f8
Source1:	http://ep09.pld-linux.org/~havner/aqua-wallpapers.tar.bz2
# Source1-md5:	a18467bf8195ee7ad0472aff57a6770e
Source2:	http://www.kde-look.org/content/files/8993-AquaBaghira-0.5.tar.gz
# Source2-md5:	d5fbd627b8f50a0c24ccd1610e8cd248
Source3:	http://www.kde-look.org/content/files/9157-kde1_1024x768.jpg
# Source3-md5:	39319dcbeb8d7b315a29e9adfffe1885
Source4:	http://www.kde-look.org/content/files/9156-kde1_1280x1024.jpg
# Source4-md5:	fb60d3af4ee9fe45006a53ba3b58e178
Source5:	http://www.kde-look.org/content/files/9155-kde1_1600x1200.jpg
# Source5-md5:	d69b3c47c32f9b87705e4f9ae0f84747
Source6:	http://www.kde-look.org/content/files/9154-Aqua1_1024x768.jpg
# Source6-md5:	907a13744968b1980b58c0b2ef8a0c1d
Source7:	http://www.kde-look.org/content/files/9153-Aqua1_1280x1024.jpg
# Source7-md5:	b08fa75e30ffed1fc2c739d858d776c0
Source8:	http://www.kde-look.org/content/files/9152-Aqua1_1600x1200.jpg
# Source8-md5:	ac3ee4acd3966cdb616c23e283ecede8
Source9:	ftp://distfiles.pld-linux.org/src/%{_name}-ksplash.tar.gz
# Source9-md5:	466cee31900639b5d633f008890b9f18
Source10:	Baghira-Lime.kcsrc
URL:		http://www.kde-look.org/content/show.php?content=8692
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRequires:	kdebase-devel
Requires:	kde-decoration-%{_name}
Requires:	kde-style-%{_name}
Requires:	kde-colorscheme-%{_name}
Requires:	kde-wallpaper-%{_name}
Requires:	kde-splashplugin-%{_name}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} KDE theme.

%description -l pl.UTF-8
Motyw KDE %{_name}.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl.UTF-8):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
%{_name} is a slicker style that was designed to look nice with
slicker. To developer's surprise, this style looks good even without
slicker.

%description -n kde-style-%{_name} -l pl.UTF-8
%{_name} to styl stworzony by współgrał z aplikacją slicker. Ku
zaskoczeniu twórców, styl ten jednak okazał się pięknie wyglądać nawet
bez slickera.

%package -n kde-icons-%{_name}
Summary:	KDE icon theme - %{_name}
Summary(pl.UTF-8):	Motyw ikon do kde - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-icons-%{_name}
%{_name} is an icon them.

%description -n kde-icons-%{_name} -l pl.UTF-8
%{_name} to motyw ikon.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl.UTF-8):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
Color scheme for KDE style - %{_name}.

%description -n kde-colorscheme-%{_name} -l pl.UTF-8
Schemat kolorów do stylu KDE - %{_name}.

%package -n kde-wallpaper-%{_name}
Summary:	KDE wallpaper - %{_name}
Summary(pl.UTF-8):	Tapeta do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-wallpaper-%{_name}
A wallpaper to go with KDE %{_name} theme.

%description -n kde-wallpaper-%{_name} -l pl.UTF-8
Tapeta pasująca do motywu %{_name}.

%package -n kdm-user-pictures-%{_name}
Summary:	KDM user picture - %{_name}
Summary(pl.UTF-8):	Obrazki dla użytkowników w KDM - %{_name}
Group:		Themes
Requires:	kdm

%description -n kdm-user-pictures-%{_name}
KDM user picture - %{_name}.

%description -n kdm-user-pictures-%{_name} -l pl.UTF-8
Obrazki dla użytkowników w KDM - %{_name}.

%package -n kde-splashplugin-%{_name}
Summary:	ksplash plugin %{_name}
Summary(pl.UTF-8):	Wtyczka ksplash %{_name}
Group:		X11/Amusements
Requires:	kdebase-desktop

%description -n kde-splashplugin-%{_name}
ksplash plugin %{_name}.

%description -n kde-splashplugin-%{_name} -l pl.UTF-8
Wtyczka ksplash %{_name}.

%package -n kde-colorscheme-%{_name}-thinkeramik
Summary:	Color scheme for %{_name} theme to go with thinkeramik style
Summary(pl.UTF-8):	Schemat kolorów dla motywu %{_name} pasujący do stylu thinkeramik
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-thinkeramik >= 3.1.4

%description -n kde-colorscheme-%{_name}-thinkeramik
Color scheme for %{_name} theme to go with thinkeramik style.

%description -n kde-colorscheme-%{_name}-thinkeramik -l pl.UTF-8
Schemat kolorów dla motywu %{_name} pasujący do stylu thinkeramik.

%package -n kde-colorscheme-%{_name}-activeheart
Summary:	Color scheme for %{_name} theme to go with activeheart style
Summary(pl.UTF-8):	Schemat kolorów dla motywu %{_name} pasujący do stylu activeheart
Group:		Themes
Requires:	kdebase-core
Requires:	kde-style-activeheart >= 1.1.7-2

%description -n kde-colorscheme-%{_name}-activeheart
Color scheme for %{_name} theme to go with thinkeramik style.

%description -n kde-colorscheme-%{_name}-activeheart -l pl.UTF-8
Schemat kolorów dla motywu %{_name} pasujący do stylu thinkeramik.

%package -n kde-splash-%{_name}
Summary:	Splash screen %{_name} theme
Summary(pl.UTF-8):	Obrazek startowy dla motywu %{_name}
Group:		Themes
Requires:	kdebase-desktop >= 9:3.1.90

%description -n kde-splash-%{_name}
Splash screen %{_name} theme.

%description -n kde-splash-%{_name} -l pl.UTF-8
Obrazek startowy dla motywu %{_name}.

%package -n kde-kside-%{_name}
Summary:	Kicker sidebar from %{_name}
Summary(pl.UTF-8):	Boczny pasek do menu kde z motywu %{_name}
Group:		Themes
Requires:	kdebase-kicker >= 9:3.1.90.030726-2
Provides:	kde-kside
Obsoletes:	kde-kside

%description -n kde-kside-%{_name}
Kicker sidebar from %{_name}.

%description -n kde-kside-%{_name} -l pl.UTF-8
Boczny pasek do menu kde z motywu %{_name}.

%package -n kopete-emoticons-%{_name}
Summary:	Kopete emoticons from %{_name} theme
Summary(pl.UTF-8):	Emotikony do kopete z tematu %{_name}
Group:		Themes
Requires:	kdenetwork-kopete

%description -n kopete-emoticons-%{_name}
Kopete emoticons from %{_name} theme.

%description -n kopete-emoticons-%{_name} -l pl.UTF-8
Emotikony do kopete z tematu %{_name}.

%package -n kde-decoration-icewm-%{_name}
Summary:	Icewm window decoration for kwin - %{_name}
Summary(pl.UTF-8):	Dekoracja icewm dla kwin - %{_name}
Group:		Themes
Requires:	kde-decoration-icewm

%description -n kde-decoration-icewm-%{_name}
Icewm window decoration for kwin - %{_name}.

%description -n kde-decoration-icewm-%{_name} -l pl.UTF-8
Dekoracja icewm dla kwin - %{_name}.

%package -n kde-decoration-%{_name}
Summary:	Kwin decoration - %{_name}
Summary(pl.UTF-8):	Dekoracja kwin - %{_name}
Group:		Themes
Requires:	kdebase-desktop-libs

%description -n kde-decoration-%{_name}
Kwin decoration - %{_name}.

%description -n kde-decoration-%{_name} -l pl.UTF-8
Dekoracja kwin - %{_name}.

%prep
%setup -q -n %{_name}-%{_name_ver} -a1 -a2 -a9

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_iconsdir}"; export kde_icondir
cp -f /usr/share/automake/config.sub admin
##export UNSERMAKE=/usr/share/unsermake/unsermake
##%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes
install colorscheme/*.kcsrc $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes

# install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
# echo "OnlyShowIn=KDE;" >> $RPM_BUILD_ROOT%{_desktopdir}/kde/kstyle_baghira_config.desktop

install -d $RPM_BUILD_ROOT%{_datadir}/wallpapers
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/wallpapers/baghira-1024x768.jpg
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/wallpapers/baghira-1280x1024.jpg
install %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/wallpapers/baghira-1600x1200.jpg
install %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/wallpapers/aqua-baghira-1024x768.jpg
install %{SOURCE7} $RPM_BUILD_ROOT%{_datadir}/wallpapers/aqua-baghira-1280x1024.jpg
install %{SOURCE8} $RPM_BUILD_ROOT%{_datadir}/wallpapers/aqua-baghira-1600x1200.jpg
install %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes/Lime\ Baghira.kcsrc
install aqua-wallpapers/* $RPM_BUILD_ROOT%{_datadir}/wallpapers/

install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes
cd AquaBaghira-0.5/Splash
for I in *; do
	cp -r $I $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/$I-Classic
	cp -r $I $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/$I-Snow
done
cd ../Bar/Classic
for I in *; do
	cp -r $I/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/$I-Classic/
done
cd ../Snow
for I in *; do
	cp -r $I/* $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/$I-Snow/
done

cd ../../../baghira-ksplash
cp -r * $RPM_BUILD_ROOT%{_datadir}/apps/ksplash/Themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files

%files -n kde-decoration-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
%{_libdir}/kde3/kstyle_baghira_config.la
%attr(755,root,root) %{_libdir}/kde3/kstyle_baghira_config.so
%{_libdir}/kde3/konqsidebar_baghirasidebar.la
%attr(755,root,root) %{_libdir}/kde3/konqsidebar_baghirasidebar.so
%{_libdir}/libbaghirastarter.la
%attr(755,root,root) %{_libdir}/libbaghirastarter.so
%{_libdir}/usermanager_panelapplet.la
%attr(755,root,root) %{_libdir}/usermanager_panelapplet.so
%{_libdir}/kde3/b_menu_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/b_menu_panelapplet.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc
%{_datadir}/apps/kicker/applets/*.desktop
%{_datadir}/apps/konqsidebartng/*/*.desktop
%dir %{_datadir}/apps/baghira
%{_datadir}/apps/baghira/poof.png
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/crystalsvg/*/*/*

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc

%files -n kde-wallpaper-%{_name}
%defattr(644,root,root,755)
%{_datadir}/wallpapers/*

%files -n kde-splashplugin-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/*
