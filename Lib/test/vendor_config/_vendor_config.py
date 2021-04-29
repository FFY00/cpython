EXTRA_SITE_INSTALL_SCHEMES = {
    'some_vendor': {
        'stdlib': '{installed_base}/{platlibdir}/python{py_version_short}',
        'platstdlib': '{platbase}/{platlibdir}/python{py_version_short}',
        'include':
            '{installed_base}/include/python{py_version_short}{abiflags}',
        'platinclude':
            '{installed_platbase}/include/python{py_version_short}{abiflags}',
        'purelib': 'vendor-pure-packages',
        'platlib': 'vendor-plat-packages',
        'scripts': 'vendor-scripts',
        'data': 'vendor-data',
    },
}
