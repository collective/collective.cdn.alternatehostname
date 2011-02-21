.. contents:: Table of Contents
   :depth: 2

CDN Support for Plone: Altenate Hostname
*******************************************

Overview
========
This package provides support for an alternate hostname CDN config for 
Plone sites.

This provider allows you to designate an alternate hostname to serve skin 
resources for your portal.
 
A very basic example would be to add 127.0.0.1 as an alternate hostname -- 
using same port number as your zope instance -- during development, thus enabling 
resources to be downloaded from 127.0.0.1 while content will be served from 
localhost.


Requirements
=============

   * Plone 3.3.x (http://plone.org/products/plone)
   * Plone 4.0.x (http://plone.org/products/plone)
   * collective.cdn.core (http://pypi.python.org/pypi/collective.cdn.core)
       
Installation
=============
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``collective.cdn.alternatehostname``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            collective.cdn.alternatehostname
    

If another package depends on the collective.cdn.alternatehostname egg or 
includes its zcml directly you do not need to specify anything in the 
buildout configuration: buildout will detect this automatically.

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the CDN Support for Plone (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource 
registries in order to see the effects of the product installation.

Usage
============

CDN settings
----------------
After installing this package, go to the 'Site Setup' page in the 
Plone interface and click on the 'CDN Configuration' link.

In this page you can choose which registries will use the CDN settings 
by clicking the respective checkboxes.

Choose the AlternateHostname provider, add a new hostname, port number 
and additional path --if needed -- then save the settings.

How it works
--------------
Using the hostname provided in the settings page, we simply replace our 
Plone site root's url with the provided information.

For example, using cache.simplesconsultoria.com.br as the alternate hostname 
with port number 80 and an empty path, the link to 
simplesconsultoria_site-cachekey0549.css file would change from::

   http://www.simplesconsultoria.com.br/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css

to::
	
   http://cache.simplesconsultoria.com.br/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css

If we inform a port number different from 80, it will be appended to the 
hostname, so with a port number of 8080, the above example would 
return::

   http://cache.simplesconsultoria.com.br:8080/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css

The same will happen if we inform a path in our settings. Using 'simples' as 
our path, the first example would return::

   http://cache.simplesconsultoria.com.br/simples/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css

Advanced Usage
================

Using a different path offers you the possibility of creating a simple 
caching/cdn server for multiple sites. As an example we will consider we 
have two Plone sites, www.simplesconsultoria.com.br and www.simplesnet.com.br, 
and  we setup cache.simples.srv.br as an alternate hostname in both Plone sites.

In order to differentiate one site from the other we will set different paths
in each of them:

   * simples in www.simplesconsultoria.com.br
   * simplesnet in www.simplesnet.com.br

So each site will have the following settings:

   * www.simplesconsultoria.com.br
      * Provider: AlternateHostname
      * Hostname: cache.simples.srv.br
      * Port: 80
      * Path: simples
   
   * www.simplesnet.com.br
      * Provider: AlternateHostname
      * Hostname: cache.simples.srv.br
      * Port: 80
      * Path: simplesnet    

And a link to a file portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css,
would return for www.simplesconsultoria.com.br::

	http://cache.simples.srv.br/simples/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css
	
And for www.simplesnet.com.br::

	http://cache.simples.srv.br/simplesnet/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css

So, our frontend server must rewrite calls to **simples/** to 
www.simplesconsultoria.com.br server and calls to **simplesnet/** to the 
www.simplesnet.com.br server.

Sponsoring
===========

Development of this product was sponsored by `Simples Consultoria 
<http://www.simplesconsultoria.com.br/>`_.


Credits
========

    * Simples Consultoria (products at simplesconsultoria dot com dot br) - 
      Implementation
