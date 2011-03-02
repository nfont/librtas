%define name librtas
%define version 1.3.6
%define release 1
Summary: Libraries to provide access to RTAS calls and RTAS events.
Name: %{name}
Version: %{version}
Release: %{release}
License: IBM Common Public License (CPL) v1.0
Source:  %{name}-%{version}.tar.gz
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
The librtas shared library provides userspace with an interface
through which certain RTAS calls can be made.  The library uses
either of the RTAS User Module or the RTAS system call to direct
the kernel in making these calls.

The librtasevent shared library provides users with a set of
definitions and common routines useful in parsing and dumping
the contents of RTAS events.

%prep
%setup -q

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT


%files
%defattr(-, root, root)
/usr/share/doc/packages/%{name}/COPYRIGHT
/usr/share/doc/packages/%{name}/README
/usr/include/common.h
/usr/include/librtas.h
/usr/lib/librtas.so.%{version}
/usr/lib/libofdt.so
/usr/lib/librtas.so
/usr/lib/librtasevent.so
/usr/lib/librtasevent.so.1
/usr/lib/librtasevent.so.%{version}
/usr/include/librtasevent.h
/usr/include/librtasevent_v4.h
/usr/include/librtasevent_v6.h

/usr/lib/libofdt.so.%{version}
/usr/include/libofdt.h

%post
# Post-install script -------------------------------------------------
ln -sf /usr/lib/librtas.so.%{version} /usr/lib/librtas.so
ln -sf /usr/lib/librtas.so.%{version} /usr/lib/librtas.so.1
ln -sf /usr/lib/librtasevent.so.%{version} /usr/lib/librtasevent.so
ln -sf /usr/lib/libofdt.so.%{version} /usr/lib/libofdt.so
ldconfig

%postun
# Post-uninstall script -----------------------------------------------
if [ "$1" = "0" ] ; then        # last uninstall
    rm -f /usr/lib/librtas.so
    rm -f /usr/lib/librtasevent.so
    rm -f /usr/lib/libofdt.so
fi
ldconfig