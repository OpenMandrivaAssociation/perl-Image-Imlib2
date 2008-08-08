%define module	Image-Imlib2
%define name	perl-%{module}
%define version 2.01
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interface to the Imlib2 image library
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Image/%{module}-%{version}.tar.bz2
Buildrequires:	perl-devel
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(ExtUtils::CBuilder)
Buildrequires:	perl(ExtUtils::XSBuilder)
Buildrequires:	imlib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Image::Imlib2 is a Perl port of Imlib2, a graphics library that does image file
loading and saving as well as manipulation, arbitrary polygon support, etc. It
does ALL of these operations FAST. It allows you to create colour images using
a large number of graphics primitives, and output the images in a range of
formats.

Image::Imlib2::Polygon and Image::Imlib2::ColorRange are described following
Image::Imlib2 but may be referenced before their description.

Note that this is an early version of my attempt at a Perl interface to Imlib2.
Currently, the API is just to test things out. Not everything is supported, but
a great deal of functionality already exists. If you think the API can be
tweaked to be a bit more intuitive, drop me a line!

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorarch}/auto/Image
%{perl_vendorarch}/Image
%{_mandir}/*/*


