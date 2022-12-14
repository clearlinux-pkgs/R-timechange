#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-timechange
Version  : 0.1.1
Release  : 1
URL      : https://cran.r-project.org/src/contrib/timechange_0.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/timechange_0.1.1.tar.gz
Summary  : Efficient Manipulation of Date-Times
Group    : Development/Tools
License  : GPL-3.0
Requires: R-timechange-lib = %{version}-%{release}
Requires: R-cpp11
BuildRequires : R-cpp11
BuildRequires : buildreq-R

%description
accounting for time-zones and daylight saving times. The package includes
   utilities for updating of date-time components (year, month, day etc.),
   modification of time-zones, rounding of date-times, period addition and
   subtraction etc. Parts of the 'CCTZ' source code, released under the Apache
   2.0 License, are included in this package. See

%package lib
Summary: lib components for the R-timechange package.
Group: Libraries

%description lib
lib components for the R-timechange package.


%prep
%setup -q -n timechange
cd %{_builddir}/timechange

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667874614

%install
export SOURCE_DATE_EPOCH=1667874614
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/timechange/DESCRIPTION
/usr/lib64/R/library/timechange/INDEX
/usr/lib64/R/library/timechange/Meta/Rd.rds
/usr/lib64/R/library/timechange/Meta/features.rds
/usr/lib64/R/library/timechange/Meta/hsearch.rds
/usr/lib64/R/library/timechange/Meta/links.rds
/usr/lib64/R/library/timechange/Meta/nsInfo.rds
/usr/lib64/R/library/timechange/Meta/package.rds
/usr/lib64/R/library/timechange/NAMESPACE
/usr/lib64/R/library/timechange/NEWS.md
/usr/lib64/R/library/timechange/R/timechange
/usr/lib64/R/library/timechange/R/timechange.rdb
/usr/lib64/R/library/timechange/R/timechange.rdx
/usr/lib64/R/library/timechange/help/AnIndex
/usr/lib64/R/library/timechange/help/aliases.rds
/usr/lib64/R/library/timechange/help/paths.rds
/usr/lib64/R/library/timechange/help/timechange.rdb
/usr/lib64/R/library/timechange/help/timechange.rdx
/usr/lib64/R/library/timechange/html/00Index.html
/usr/lib64/R/library/timechange/html/R.css
/usr/lib64/R/library/timechange/tests/testthat.R
/usr/lib64/R/library/timechange/tests/testthat/test-addition.R
/usr/lib64/R/library/timechange/tests/testthat/test-get.R
/usr/lib64/R/library/timechange/tests/testthat/test-round.R
/usr/lib64/R/library/timechange/tests/testthat/test-time-zones.R
/usr/lib64/R/library/timechange/tests/testthat/test-update.R
/usr/lib64/R/library/timechange/tests/testthat/utils.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/timechange/libs/timechange.so
/usr/lib64/R/library/timechange/libs/timechange.so.avx2
/usr/lib64/R/library/timechange/libs/timechange.so.avx512
