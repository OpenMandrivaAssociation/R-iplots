%global packname  iplots
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.1_4
Release:          2
Summary:          iPlots - interactive graphics for R
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-4.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-methods R-rJava 
Requires:         R-maps R-MASS 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-rJava
BuildRequires:    R-maps R-MASS 
BuildRequires:    java-rpmbuild
BuildRequires:    x11-server-xvfb

%description
Interactive plots for R

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
xvfb-run %{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
mkdir -p %{buildroot}%{_javadir}/iplots.jar
ln -sf %{rlibdir}/java/iplots.jar %{buildroot}%{_javadir}/iplots.jar

# FIXME wants to test (disabled/removed dependency) R-CarbonEL OS-X interface
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/java
%{_javadir}/iplots.jar
