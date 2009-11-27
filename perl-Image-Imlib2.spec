%define upstream_name    Image-Imlib2
%define upstream_version 2.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Interface to the Imlib2 image library
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:  imlib2-devel
Buildrequires:  perl(Module::Build)
Buildrequires:  perl(ExtUtils::CBuilder)
Buildrequires:  perl(ExtUtils::XSBuilder)
Buildrequires:  perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
%setup -q -n %{upstream_name}-%{upstream_version}

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
