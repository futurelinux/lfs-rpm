Name:           lfs-bash
Version:        5.2.15
Release:        1%{?dist}
Summary:        Toolchain for building LFS
License:        GPL

Source0:        https://ftp.gnu.org/gnu/bash/bash-%{version}.tar.gz

%undefine       _auto_set_build_flags
%global         debug_package %{nil}


%description
Toolchain for building LFS


%prep
%setup -q -n bash-%{version}


%build
%lfs_path
./configure --prefix=/usr                      \
            --build=$(sh support/config.guess) \
            --host=%{lfs_tgt}                  \
            --without-bash-malloc
make


%install
%lfs_path
make DESTDIR=%{buildroot}/%{lfs} install
mkdir -p %{buildroot}/%{lfs}/bin
ln -s bash %{buildroot}/%{lfs}/usr/bin/sh
%lfs_remove_docs


%files
%{lfs}/usr/bin/*
%{lfs}/usr/include/bash
%{lfs}/usr/lib/bash
%{lfs}/usr/lib/pkgconfig/bash.pc
%{lfs}/usr/share/locale/*/LC_MESSAGES/bash.mo


%changelog
* Wed Oct 4 2023 Mike McGann <mike.mcgann@blackchip.org> - 5.2.15-1
- Initial package

