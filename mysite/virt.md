
- **Overhead:** Additional layers and emulation can lead to increased resource usage and slower performance.

## Describe why network/shared storage is most often used for storing virtual disks of VMs
- **Flexibility:** Network/shared storage allows VMs to be easily moved between hosts, enhancing flexibility and scalability.

## VCenter
- Centralized management for VMware environments.

## Live Migration
- The ability to move a running VM from one host to another without downtime.

## Hyper-V (WSL, VBS functionality)
- **WSL (Windows Subsystem for Linux):** Allows running Linux applications on Windows.
- **VBS (Virtualization-Based Security):** Security features in Hyper-V.
- hyper V  == Virtualisation solution for Windows
- type 1 

## Bhyve
- Type 2 hypervisor for hardware virtualization.
- bhyve är utformat för att leverera hög prestanda, skalbarhet och effektiv hantering av virtualiserade miljöer.
- HW level vritualization

## FreeBSD Jails
- OS-level virtualization on FreeBSD.
- Jails möjliggör partitionering och skapande av oberoende miljöer på en FreeBSD-server, 
- vilket ger användare möjlighet att isolera processer och resurser för ökad säkerhet och systemadministration.


## KVM - Kernel Virtual Machine
- A Linux kernel module converting Linux kernel into a hypervisor.


## libvirt + QEMU + KVM -- vanligaste virtualisering stacken på linux
## Libvirt + QEMU + KVM
- Common virtualization stack on Linux.
- **Libvirt:** libvirt är en plattformsoberoende API och verktygssamling 
	för att hantera virtualiseringsplattformar,
	mess of python and xml files
	skriver filer till diskar, snapshots

- **QEMU:** QEMU kan köra gästoperativsystem utan att kräva paravirtualisering
	, men när det kombineras med KVM dra nytta av hårdvaruacceleration för att 
	förbättra prestanda
	säkerhet var inte prioritering
	kan emulera i princip allt, olika ljudkort tiollomed etc
	oerhört flexibel
	fanns en brist i floppy drive
    emulates BIOS/UEFI
    kan emulera konstriga arkitekturer


## Proxmox
- Open-source virtualization solution.
- Den kombinerar två huvudkomponenter: KVM-virtualisering för virtualisering av kompletta maskiner och 
- LXC (Linux Containers) för lätta, portabla containrar.

## Cloud Hypervisor
- Emulates and hosts virtual servers, a replacement for QEMU.

## Firecracker
- Developed by AWS for secure and high-performance virtualization.
- Written in Rust.
- virtuell disc och nätverkskort. utvecklat i rust
säkerhet och prestanda i tanken
focuses on Low-overhead VM execution
- low overhead

 ## small (TCB) Trusted computer base

## TCB -- 
	lita på koden under applikationen som körs
	
	pågrund av detta används zen i qubes

## Xen -- type 1
paravirtuallisering- inte låtsas vara fysisk hårdvara
Dom0 pratar med hypervisorn för att skapa virtualisering
samarbetar effektift med hypervisorn. paravirtualisering

## Whonix
- An operating system focused on anonymity, privacy, and security.

## Edge Computing
- Reducing latency by moving computing resources closer to the user.

## Confidential Computing
- Ensuring data confidentiality even when processed in untrusted environments.
- syftar till att skydda känslig information även när den bearbetas av molnresurser eller andra externa enheter.
- Realtidsrespons:
- IoT och sensorer:


## Memory Encryption
- **AMD SEV:** Encrypts memory to enhance security.

## Cold Boot Attack
- Retrieving encryption keys from a powered-down system.

## Full Guest Isolation
- Ensures complete isolation between virtual machines.
är en teknik inom virtualisering där en virtuell maskin (VM) 
har ingen medvetenhet om att den körs i en virtuell miljö

## CPU Assisted Virtualization
- Saves CPU cycles, reduces latency in memory writes.
- sparar cpu cyklar, sparar latens mellan minnes skrivningar

## Feature Masking
- Hides specific functionality.


## Memory Ballooning
- Dynamically adjusts resources based on usage.
- skiftar om resusreser utefter användningen så att tex datorn inte är låst att ha 8gb ram om
- den endast använder 3gb tex

## Vertical Scaling
- Increasing or decreasing power in terms of CPU, RAM.

## Horizontal Scaling
- Adding or removing VM´s

## Nested Virtualization
- Virtualized environment within a virtualized environment.

## OS-Level Virtualization
- Pretends to be an operating system environment.

## Lixuulator and Windows WSL v1
- Allows running many Linux apps on Windows.

## Wine
- Allows running Windows apps on Linux and Mac.

## Edge computing --

	Sammanfattningsvis handlar edge computing om att ta
	databehandlingen närmare användaren eller den plats där 
	data genereras för att uppnå snabbare och mer effektiva svar,

## Syscodes
- System calls monitoring.

## User Space / Kernel Space
- Shared kernel, more efficient scheduling.

## One Way Mirror
- Monitors guests for malicious activity.

## Falco
- Configurable rules for alerts.

## Cuco
- (Content Missing)


## Capabilities
- Define privileges for processes.

## Proxmox Server
- Segmenting public sites from the rest.
- Setting up virtual bridges and machines.

## Paravirtualization
innebär att ett gästoperativsystem modifieras för att vara medvetet om och samarbeta med en hypervisormiljö.
- Guest OS is consciously modified.
- More guests to be run on the same host

## Full Virtualization
- Guest OS is unaware of being virtualized.

## VPC - Virtual Private Cloud
- Private space in the public cloud.
- Regions, CIDR, DHCP settings, DNS route table.


## On premises
	att fysiska hårdvaran är på eller ägs av företaget
	som använder det till sig själva


## AUTOMATION- ClickOps
	clickops är att processen att klicka fram och konfigurera
	automatisering löser detta
	

## Jumpbox
	kind of like a VPN, en säker server som används som en första
	stopp innan anslutning utåt sker

## VPN
     direct connect - dedicated pipe to the cloud


## overhead = slower


## Cloud Init

	verktyg för att konfigurera nya VM när dom startar första gången
	kan göras genom skript, konfigurationsfiler 


## IaaC= infrastructure as a code 
	make infrastructure work on every cloud supporting the tool
	HashiCorp Terraform är populärt 
	OpenTofu är opensource kusinen

## SaaS -- software as service
- du behöver bara använda tjänste, exempel är netflix spotify etc.
- man behöver inte göra nåbting
	per per use on demand
	no installment
	resources managed by vendor
	via webbläsare
	provider ansvarig för allt som skalbarhet osv
	man vet inte vart datat lagras, maktlös, oklar framtid

	

## PAAS -- platform as a service
- man får ett API till en platform som tar hand om resten som databaser, webservrar
	färdiga system att deploya sin kod
	ladda upp källkod till platform som kompilerar
	säkerheten -- du måste lita på provider
	kan bli locked in
	enkelt och kostnadseffektiv

	

## IAAS -- infrastructure as a service

	Man har kontroll över infra strukturen
	vps - cloud instans.
	man hyr cpu, ram, lagring
	klöper resureser vid behov, ökar o minskqar
	kan undvika locking med opensource lösningar
	
## CAAS -- container as a service

	betalar för container orkestrerring
	kuberenetes
	skalbarehet, resurseffektivt jämfört med VM
	upload elsewhere

## FAAS -- function as a sevice

	köper enskilda API anrop
	pay per cpu cycles used.
	djupt bunden. Locked in
	leverantören skrivs utifrån leveratören


## Bladservrar 
	shared management --
	signal backplane --  
	compute blade -- 

## cluster

två eller flera datorer som bildar en logisk enhet
bildar spegling sinsemellan, minskad downtime

# aktiv-aktiv cluster ---
    -- hantera både läsning och skrivningar, realtids spegling
    dyrare, avbrottsfritt, svårare att konfigurerar

# aktiva passiv cluster ---
    -- en server är huvud server. den andra är passiv, data skickas åt ett håll.
    går den aktiva servern ner så aktiveras den passiva


## KVM -- 
	KVM är en Linux-kärnemodul som omvandlar
	Linux-kärnan till en hypervisor.
	

## QEMU --
	QEMU kan köra gästoperativsystem utan att kräva paravirtualisering
	, men när det kombineras med KVM dra nytta av hårdvaruacceleration för att 
	förbättra prestanda
	säkerhet var inte prioritering
	kan emulera i princip allt, olika ljudkort tiollomed etc
	oerhört flexibel
	fanns en brist i floppy drive
- Application that emulates hardware devices for VMs
- primary focus Flexibility
	
### ESXI
	produkt av VMWARE
	directly installed on hardware
    ESXi möjliggör virtualisering av serverresurser, inklusive processorer, 
    minne, lagring och nätverk.
	
## Libvirt --
	libvirt är en plattformsoberoende API och verktygssamling 
	för att hantera virtualiseringsplattformar,
	mess of python and xml files
	skriver filer till diskar, snapshots

# virtIO

Virtio möjliggör kommunikation för olika typer av I/O-enheter, såsom nätverkskort,
lagringsenheter och andra enheter, mellan gäst- och värdsystem.
- Para virtualiserad hårdvara -- LÅTSAS INTE vara fysisk hårdvara
- Creates a fast communication pathway between virtual machines and hosts.
	

 ## Linux LXC / Linux LXD
- Linux containerization solutions.

## Daemon
- Background system services.

## Network Namespaces / User Namespace
- Används för att isolera resurser och processer i linux miljö. 
- möjliggör skapande av isolerade och oberoende nstanser i systemresurser
- PID Namespace (pid): Isolerar process-ID:er. Processer inom en PID-namespace ser bara andra processer inom samma namespace.
- Network Namespace (net): Isolerar nätverksresurser som nätverkssnitt, routetabeller och brandväggar. Varje nätverksnamespace har sina egna nätverksresurser.
- kmedlemmarna i ett namespace ser endast det som dom har i sitt namespace
- 

## chroot

isolerar chroot en process och dess eventuella underordnade processer till en annan mapp,
 vilket får dem att tro att den nya mappen är rotkatalogen för filsystemet.


## Cgroup
- Cgroups möjliggör därmed resurskontroll och isolation på en Linux-systemnivå.
- Den tillåter en finjustering av hur mycket CPU-tid, minne, nätverksbandbredd och andra systemresurse

## Linux Netfilter
- uppsättning ramverk inom Linux-kärnan som möjliggör för hantering av nätverkstrafik genom att tillhandahålla funktioner för filtrering,

## Systemd-cgtop
- Verktyget ger realtidsinformation om hur mycket CPU-tid, 
- minne och andra resurser olika systemd cgroups använder på systemet.

## Seccomp
- "secure computing", är en Linux-kärnemekanism som används 
- för att begränsa vilka systemanrop som en process kan göra.
- (brandvägg för systemcalls)
- man kan tex låt en tjänst bara prata med vissa porta, eller skicka med vissa argument.
- använda specifika systemanrop man anser vara okej/säkra


## noisy neighbour 
    när olika  maskiner som delar samma kärna stör ut varandra 

## cpu pinning
    begränsa vilka tjänster som får använda specifika kärnor
    då linux schemalägger vilka processer som skall få diverse cpu kraft så styr man dett med cpu pinning


# Vagrant
- Vagrant är en mjukvara för automatiserad hantering av virtuella utvecklingsmiljöer. 
- Den är utformad för att underlätta skapandet, distributionen och hanteringen av virtuella maskiner
- skapa konsistenta och återanvändbara utvecklingsmiljöer.

# Docker
Docker är främst en plattform för containerization. En container är en körbar enhet som innehåller 
allt som behövs för att köra en programvara, inklusive kod, runtime, systemverktyg och bibliotek
- kompabilitet men lägre säkerhetstänk

## VM SPRAWL
 när det finns en överdriven och ohanterad tillväxt av virtuella maskiner (VM) inom en IT-infrastruktur. 
 Det uppstår när organisationer skapar och distribuerar virtuella maskiner på ett sätt som leder till ökad komplexitet

# unikernels 
minimala operativsystemkärnor som är utformade för att köra som en enda enhetlig image
lågt overhead
säkert
effektivt
provides a predictable runtime environment

## QUIZEN !!
## deduplication of guest storage
Disk space is saved by only storing the same data once


# qubes 
- relies on xen 
- high security
- containerization

# paravirtualkisering 
- aims to improve performance

# another commonly used term for os virtualisation 
is containers

## PCI forwarding
Genom att använda PCI forwarding kan en virtuell maskin direkt kommunicera med och 
kontrollera den dedikerade PCI-enheten utan att gå genom värdoperativsystemet eller hypervisorn.


## LXC is example
OS-level virtualisation

## LXD supports
HW- and OS-level virtualisation
kan skapa virtuella maskiner på OS nivå men även med hhjälp av qemu på HW nivå

## runc
implementation av Open Container Initiative
- os-level virtualisering
- containerd och docker använder detta 

# HYPER V
HW-level virtualisation

# chroot restrict 
File system access

# cgroup
Limit access to system resources

# VDI
Virtual Desktop Infrastructure

# racks 19 rack 
# 1u 
# OCP standard, giganter som bildat en standard 

# Terraform
 Det används för att automatisera och hantera infrastrukturtillgångar som servrar, nätverk, lagringsutrymme och andra molnresurser. 
 IaC infrastructure as code


## Ansible
Ansible är ett öppen källkodsverktyg för automatisering, konfigurationshantering och driftsättning.
- skrivet i python
  

## Openstack and cleura

hypervisor - KVM & qemu
API - Libvirt

images do not mean pictures - meaning operating system images

# NOVA 
- erbjuder skalbara och distribuerade beräkningsresurser genom att hantera skapandet och hanteringen av virtuella maskiner.
-  Nova stöder olika hypervisors, möjliggör nätverkshantering, har ett API-gränssnitt för användarinteraktion, 
-  integreras med Keystone för autentisering
  
# Neutron
- SDN networking project
- NaaS network as a service
    define network structure.

# Cinder
- active passive cluster
- block storage
  
# Swift 
- object storage  -- its kinda like a google drive
  allow to store and read seperate files.
  distribute across multiple maschines.
  accessed programatically - used 

object storage -- 
Object storage i molnet är en enkel och effektiv metod för att lagra och hantera stora mängder data. Istället för att 
organisera data i traditionella filstrukturer eller blockbaserade system, lagrar object storage data som objekt. 
Varje objekt har en unik identifierare och innehåller själva datan tillsammans med metadata och en adress för att hämta objektet.

# Glance
- images service , register and retrieving
- can search on keywords in images

# horizon 
implementation of the dashboard

# octavia (LBaaS)
- load balancer as a service
- configures load balance to sspecific servers
- based on HAproxy
- SSL , L7 routing
- stores certificates BARBICAN
  
  # Barbican - Secrets 
  - encryption keys
  - certificate 

# Keystone
- authentication 
- LDAP, OATH , OPENID connect, SAML and SQL

# Heat
- orchestrates volumes and other resources via YAML templates
- IaaC
  
# IaaC
- Declarative
- define desired state and tool will try figure out and configure for you
Terraform 

Version control
    important part
    track changes over time in folder structure.

# Git 


# IaC tools
saltstack
aws cloudformation
# Terraform
    manages infrastructures life cycle
    HCL language
    can read json configures
- State - - muste store a state about the infrastructure
- localfiel terraform.tfstate
can store the file publicly about the infrastructure so multiple people share same state

download rc file
source it
put password

