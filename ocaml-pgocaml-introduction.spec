Name:           ocaml-pgocaml-introduction
Version:        0.92
Release:        %mkrel 1
Summary:        A Brief Introduction to PG'OCaml
License:        CC-by-sa-3.0
Group:          Development/Other
URL:            http://www.dse.nl/~dario/projects/pgoctut/
Source0:        http://www.dse.nl/~dario/projects/pgoctut/pgoctut.pdf.lzma
# Real:         http://www.dse.nl/~dario/projects/pgoctut/pgoctut.pdf
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildArch:      noarch

%description
PG'OCaml, by Richard W. M. Jones, provides an interface to PostgreSQL
databases for OCaml applications. It uses  Camlp4 to extend the OCaml
syntax, enabling one to directly embed SQL statements inside the OCaml
code. Moreover, it uses the describe feature of PostgreSQL to obtain
type information about the database. This allows PG'OCaml to check at
compile-time if the programme is indeed consistent with the database
structure. This type-safe database access is the primary advantage that
PG'OCaml has over other PostgreSQL bindings for OCaml.

Unfortunately, PG'OCaml is rather lacking on the documentation front.
This document aims to fill that gap, by providing an overview of the
capabilities of the library, usage examples, and solutions to potential
pitfalls. Moreover, it also addresses the installation of PG'OCaml,
how to compile programmes that make use of the library, and the
correspondence between PostgreSQL data types and their OCaml
counterparts.

%prep
lzcat %{SOURCE0} > pgoctut.pdf

%build

%install
rm -rf %{buildroot}
%define destdir %{_datadir}/doc/%{name}
mkdir -p %{buildroot}%{destdir}
install -d -m 755 %{buildroot}%{destdir}
install -m 644 pgoctut.pdf %{buildroot}%{destdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{destdir}
%{destdir}/pgoctut.pdf

