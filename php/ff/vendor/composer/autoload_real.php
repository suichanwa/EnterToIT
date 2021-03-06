<?php

// autoload_real.php @generated by Composer

class ComposerAutoloaderInit30b4f7e68d1deffa57e5e3fd86a63789
{
    private static $loader;

    public static function loadClassLoader($class)
    {
        if ('Composer\Autoload\ClassLoader' === $class) {
            require __DIR__ . '/ClassLoader.php';
        }
    }

    /**
     * @return \Composer\Autoload\ClassLoader
     */
    public static function getLoader()
    {
        if (null !== self::$loader) {
            return self::$loader;
        }

        require __DIR__ . '/platform_check.php';

        spl_autoload_register(array('ComposerAutoloaderInit30b4f7e68d1deffa57e5e3fd86a63789', 'loadClassLoader'), true, true);
        self::$loader = $loader = new \Composer\Autoload\ClassLoader(\dirname(__DIR__));
        spl_autoload_unregister(array('ComposerAutoloaderInit30b4f7e68d1deffa57e5e3fd86a63789', 'loadClassLoader'));

        require __DIR__ . '/autoload_static.php';
        call_user_func(\Composer\Autoload\ComposerStaticInit30b4f7e68d1deffa57e5e3fd86a63789::getInitializer($loader));

        $loader->register(true);

        return $loader;
    }
}
