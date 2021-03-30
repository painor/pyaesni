pyaesni
=======

a cpython bindings to libaesni which is a binding to intel aes ni.

installation
------------

If you want to install it yourself then you’re going to need a yasm
compiler. you can get it from here
https://yasm.tortall.net/Download.html

You can also download it from pip if a wheel is available for your
device.
::

    pip install pyaesni

Usage
-----

Usage is pretty simple.

.. code:: python

   import pyaesni
   encrypted = pyaesni.ige256_encrypt(data, key, iv)

everything is a buffer there. you can check the examples folder for more

available methods
-----------------

::

   ige256_encrypt
   ige256_decrypt
   ctr256_encrypt
   ctr256_decrypt
   cbc256_encrypt
   cbc256_decrypt

credits
~~~~~~~

`wirtos`_ for doing most of the stuff and compilation

`painor`_ me for motivating him (and some setup.py stuff)

`dan`_ for the cpython boilerplate

.. _wirtos: https://github.com/Wirtos
.. _painor: https://github.com/painor
.. _dan: https://github.com/delivrance
