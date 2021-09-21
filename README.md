<img src="https://rawgit.com/Spirals-Team/powerapi/master/resources/logo/PowerAPI-logo.png" alt="Powerapi" width="300px">

[![Join the chat at https://gitter.im/Spirals-Team/powerapi](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Spirals-Team/powerapi?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![License: BSD 3](https://img.shields.io/pypi/l/powerapi.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Build Status](https://img.shields.io/circleci/project/github/powerapi-ng/powerapi.svg)](https://circleci.com/gh/powerapi-ng/powerapi)

PowerAPI is a middleware toolkit for building software-defined power meters.
Software-defined power meters are configurable software libraries that can estimate the power consumption of software in real-time.
PowerAPI supports the acquisition of raw metrics from a wide diversity of sensors (_eg._, physical meters, processor interfaces, hardware counters, OS counters) and the delivery of power consumptions via different channels (including file system, network, web, graphical).
As a middleware toolkit, PowerAPI offers the capability of assembling power meters _«à la carte»_ to accommodate user requirements.

# About

PowerAPI is an open-source project developed by the [Spirals research group](https://team.inria.fr/spirals) (University of Lille 1 and Inria) and fully managed with [setuptools](https://pypi.org/project/setuptools/).

The documentation is available [here](http://powerapi.org).

## Mailing list

You can follow the latest news and asks questions by subscribing to our <a href="mailto:sympa@inria.fr?subject=subscribe powerapi">mailing list</a>.

## Contributing

If you would like to contribute code you can do so through GitHub by forking the
repository and sending a pull request.
You should start by reading the [contribution guide](https://github.com/powerapi-ng/powerapi/blob/master/contributing.md)

When submitting code, please make every effort to follow existing conventions and style in order to keep the code as readable as possible.

## Publications

- **[Power Budgeting of Big Data Applications in Container-based Clusters](https://hal.inria.fr/hal-02904300)**: J. Enes, G. Fieni, R. Expósito, R. Rouvoy, J. Tourino. _IEEE Cluster_, September 2020, Kobe, Japan
- **[SmartWatts: Self-Calibrating Software-Defined Power Meter for Containers](https://hal.inria.fr/hal-02470128)**: G. Fieni, R. Rouvoy, L. Seinturier. _IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing_ (CCGrid). May 2020, Melbourne, Australia
- **[Taming Energy Consumption Variations in Systems Benchmarking](https://hal.inria.fr/hal-02403379)**: Z. Ournani, M.C. Belgaid, R. Rouvoy, P. Rust, J. Penhoat, L. Seinturier. _ACM/SPEC International Conference on Performance Engineering_ (ICPE). April 2020, Edmonton, Canada
- **[WattsKit: Software-Defined Power Monitoring of Distributed Systems](https://hal.inria.fr/hal-01439889)**: M. Colmant, P. Felber, R. Rouvoy, L. Seinturier. _IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing_ (CCGrid). April 2017, Spain, France
- **[Process-level Power Estimation in VM-based Systems](https://hal.inria.fr/hal-01130030)**: M. Colmant, M. Kurpicz, L. Huertas, R. Rouvoy, P. Felber, A. Sobe. _European Conference on Computer Systems_ (EuroSys). April 2015, Bordeaux, France
- **[Monitoring Energy Hotspots in Software](https://hal.inria.fr/hal-01069142)**: A. Noureddine, R. Rouvoy, L. Seinturier. _Journal of Automated Software Engineering_, Springer, 2015
- **[Unit Testing of Energy Consumption of Software Libraries](https://hal.inria.fr/hal-00912613)**: A. Noureddine, R. Rouvoy, L. Seinturier. _International Symposium On Applied Computing_ (SAC), March 2014, Gyeongju, South Korea
- **[Informatique : Des logiciels mis au vert](http://www.jinnove.com/Actualites/Informatique-des-logiciels-mis-au-vert)**: L. Seinturier, R. Rouvoy. _J'innove en Nord Pas de Calais_, [NFID](http://www.jinnove.com)
- **[PowerAPI: A Software Library to Monitor the Energy Consumed at the Process-Level](http://ercim-news.ercim.eu/en92/special/powerapi-a-software-library-to-monitor-the-energy-consumed-at-the-process-level)**: A. Bourdon, A. Noureddine, R. Rouvoy, L. Seinturier. _ERCIM News, Special Theme: Smart Energy Systems_, 92, pp.43-44. [ERCIM](http://www.ercim.eu), 2013
- **[Mesurer la consommation en énergie des logiciels avec précision](http://www.lifl.fr/digitalAssets/0/807_01info_130110_16_39.pdf)**: A. Bourdon, R. Rouvoy, L. Seinturier. _01 Business & Technologies_, 2013
- **[A review of energy measurement approaches](https://hal.inria.fr/hal-00912996v2)**: A. Noureddine, R. Rouvoy, L. Seinturier. _ACM SIGOPS Operating Systems Review_, ACM, 2013, 47 (3)
- **[Runtime Monitoring of Software Energy Hotspots](https://hal.inria.fr/hal-00715331)**: A. Noureddine, A. Bourdon, R. Rouvoy, L. Seinturier. _International Conference on Automated Software Engineering_ (ASE), September 2012, Essen, Germany
- **[A Preliminary Study of the Impact of Software Engineering on GreenIT](https://hal.inria.fr/hal-00681560)**: A. Noureddine, A. Bourdon, R. Rouvoy, L. Seinturier. _International Workshop on Green and Sustainable Software_ (GREENS), June 2012, Zurich, Switzerland

## Use Cases

PowerAPI is used in a variety of projects to address key challenges of GreenIT:

- [GenPack](https://hal.inria.fr/hal-01403486) provides a Docker Swarm strategy to minimize the energy footprint of Docker containers deployed in a cluster
- [BitWatts](http://bitwatts.powerapi.org) provides process-level power estimation of applications running in virtual machines
- [Web Energy Archive](http://webenergyarchive.com) ranks popular websites based on the energy footpring they imposes to browsers
- [Greenspector](http://greenspector.com) optimises the power consumption of software by identifying potential energy leaks in the source code.

## Acknowledgments

We all stand on the shoulders of giants and get by with a little help from our friends. PowerAPI is written in [Python](https://www.python.org/) (under [PSF license](https://docs.python.org/3/license.html)) and built on top of:

- [pyzmq](https://github.com/zeromq/pyzmq) (under [3-Clause BSD license](https://opensource.org/licenses/BSD-3-Clause)) for inter-process communication.
- [pymongo](https://github.com/mongodb/mongo-python-driver) (under [Apache 2 license](https://github.com/mongodb/mongo-python-driver/blob/master/LICENSE)) for the MongoDB database (input/output) support.
