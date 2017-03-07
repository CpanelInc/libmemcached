# libmemcached rpm
# primiarily to be used for CentOS 6 for EasyApache 4
# CentOS 6 only provides libmemcached .31 and .44 or greater is required for php-memcached.
%global libname libmemcached

Name: %{libname}
Version: 1.0.18
Summary: libmemcached standard library for interacting with memcached
%define release_prefix 1
Release: %{release_prefix}%{?dist}.cpanel
License: BSD
Group: System Environment/Libaries
URL: http://libmemcached.org/libMemcached.html
Source: https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz

BuildRequires: libevent-devel

%description
libmemcached is a C/C++ client library and tools for the memcached server
(http://memcached.org/). It has been designed to be light on memory
usage, and provide full access to server side methods.



%package devel
Summary:    Header files and development libraries for %{name}
Group:      Development/Libraries
Requires:   pkgconfig
Obsoletes:  %{libname}10-devel       < %{version}
Conflicts:  %{libname}-devel         < %{version}
Provides:   %{libname}-devel         = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name}, 
you will need to install %{name}-devel.


%package tools
Summary:    %{libname} tools
Group:      Applications/System

%description tools
%{libname}-tools provides several command line tools for use against libmemcached:

memaslap    Load testing and benchmarking a server
memcapable  Checking a Memcached server capibilities and compatibility
memcat      Copy the value of a key to standard output
memcp       Copy data to a server
memdump     Dumping your server
memerror    Translate an error code to a string
memexist    Check for the existance of a key
memflush    Flush the contents of your servers
memparse    Parse an option string
memping     Test to see if a server is available.
memrm       Remove a key(s) from the server
memslap     Generate testing loads on a memcached cluster
memstat     Dump the stats of your servers to standard output
memtouch    Touches a key

%prep
%setup -n %{libname}-%{version}

%build
  # --prefix=%{buildroot}/%{_usr} \
./configure \
  --with-memcached=false \
  --disable-sasl \
  --enable-libmemcachedprotocol \
  --enable-memaslap \
  --enable-dtrace \
  --disable-static

make

%install
make install DESTDIR=%{buildroot}
# make install

#%check
#make test

%post
ldconfig

%postun
ldconfig

%files
%defattr (-,root,root,-)
%{_usr}/local/lib/libhashkit.so.2*
%{_usr}/local/lib/libmemcached.so.11*
%{_usr}/local/lib/libmemcachedprotocol.so.0*
%{_usr}/local/lib/libmemcachedutil.so.2*
# %{_libdir}/libhashkit.so.2*
# %{_libdir}/libmemcached.so.11*
# %{_libdir}/libmemcachedprotocl.so.0*
# %{_libdir}/libmemcachedutil.so.2*

%files tools
%defattr (-,root,root,-)
%{_usr}/local/bin/mem*
%exclude %{_usr}/local/lib/lib*.la
%{_usr}/local/share/man/man1/mem*

%files devel
%defattr (-,root,root,-)
%{_usr}/local/include/libmemcached
%{_usr}/local/include/libmemcached-1.0
%{_usr}/local/include/libhashkit
%{_usr}/local/include/libhashkit-1.0
%{_usr}/local/include/libmemcachedprotocol-0.0
%{_usr}/local/include/libmemcachedutil-1.0
%{_usr}/local/lib/libhashkit.so
%{_usr}/local/lib/libmemcached.so
%{_usr}/local/lib/libmemcachedprotocol.so
%{_usr}/local/lib/libmemcachedutil.so
%{_usr}/local/lib/pkgconfig/libmemcached.pc
%{_usr}/local/share/aclocal/ax_libmemcached.m4
%{_usr}/local/share/man/man3/libmemcached*
%{_usr}/local/share/man/man3/libhashkit*
%{_usr}/local/share/man/man3/memcached*
%{_usr}/local/share/man/man3/hashkit*

%ChangeLog
* Sat Mar  4 2017 Jack Hayhurst <jack@deleteos.com> - 0.2
- wrote initial libmemcached spec
