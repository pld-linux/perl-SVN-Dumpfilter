#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define	pdir	SVN
%define	pnam	Dumpfilter
%include	/usr/lib/rpm/macros.perl
Summary:	SVN::Dumpfilter - Perl extension to filter Subversion dumpfiles
Name:		perl-SVN-Dumpfilter
Version:	0.21
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SVN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	51636274ce0a66d70a889fb3b1911f89
URL:		http://search.cpan.org/dist/SVN-Dumpfilter/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SVN::Dumpfilter reads a Subversion <http://subversion.tigris.org/>
dumpfile.

The file is parsed and a call-back subfunction is called with a
hash-reference for every 'node'. This function can modify, add or
delete headers, properties and the content of the node. After
processing of the call-back function the node is re-assembled and
stored in an output file.

The parse and re-assemble processes are done by dedicated subfunctions
which can be also exported ('internal' tag) for special filters (e.g.
merging filter which has to write the output file by its own).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/SVN/Dumpfilter.pm
%{_mandir}/man3/*
