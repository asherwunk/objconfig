"""
This is a port of zend-config to Python

NOTE: This file requires PyYaml, which is recorded in the setup.py

Some idioms of PHP are still employed, but where possible I have Pythonized it

Author: Asher Wolfstein (http://wunk.me/)
Package Homepage: http://wunk.me/programming-projects/objconfig-python/
GitHub: http://github.com/asherwunk/objconfig for the source repository

Following is the header as given in zend-config:

/**
 * Zend Framework (http://framework.zend.com/)
 *
 * @link      http://github.com/zendframework/zf2 for the
 *            canonical source repository
 * @copyright Copyright (c) 2005-2015 Zend Technologies USA Inc.
 *            (http://www.zend.com)
 * @license   http://framework.zend.com/license/new-bsd New BSD License
 */
"""

from objconfig.reader import ReaderInterface
from objconfig.exception import RuntimeException
from objconfig.util import array_merge_recursive
import yaml
import os

"""
Following is the class documentation as given in zend-config:

/**
 * YAML config reader.
 */
"""


class Yaml(ReaderInterface):
    
    def __init__(self):
        """
        Utilize load_safe method?
        """
        self.safe = True
        
        """
        /**
         * Directory of the JSON file
         *
         * @var string
         */
        """
        self.directory = ''
    
    """
    /**
     * fromFile(): defined by Reader interface.
     *
     * @see    ReaderInterface::fromFile()
     * @param  string $filename
     * @return array
     * @throws Exception\RuntimeException
     */
    """
    def fromFile(self, filename):
        if not os.path.isfile(filename) and not os.access(filename, os.R_OK):
            raise RuntimeException("Yaml: File %s Doesn't Exist or Not Readable" % filename)
        
        self.directory = os.path.dirname(filename.rstrip(os.sep)) or '.'
        
        conf = {}
        
        try:
            with open(filename, "r") as file:
                yamlcontent = file.read()
                if self.safe:
                    conf = yaml.safe_load(yamlcontent)
                else:
                    conf = yaml.load(yamlcontent)
        except yaml.YAMLError as e:
            raise RuntimeException("Yaml: Error Reading YAML file \"%s\": %s" % (filename, e))
        
        return self.process(conf)
    
    """
    /**
     * fromString(): defined by Reader interface.
     *
     * @param  string $string
     * @return array|bool
     * @throws Exception\RuntimeException
     */
    """
    def fromString(self, string):
        if not string:
            return {}
        
        self.directory = None
        
        conf = {}
        
        try:
            if self.safe:
                conf = yaml.safe_load(string)
            else:
                conf = yaml.load(string)
        except yaml.YAMLError as e:
            raise RuntimeException("Yaml: Error Reading YAML string: %s" % e)
        
        return self.process(conf)
    
    """
    /**
     * Process the array for @include
     *
     * @param  array $data
     * @return array
     * @throws Exception\RuntimeException
     */
    """
    def process(self, array):
        for key, value in (array.items() if 'items' in dir(array) else array):
            if isinstance(value, (tuple, list, dict)):
                array[key] = self.process(value)
            elif "_@include" in key:
                if not self.directory:
                    raise RuntimeException("Yaml: Cannot Process @include When Reading From String")
                if (not os.path.isfile(os.path.join(self.directory, value))
                        and not os.access(os.path.join(self.directory, value), os.R_OK)):
                    raise RuntimeException("Yaml: File %s Doesn't Exist or Not Readable (@include)" % value)
                conf = {}
                with open(os.path.join(self.directory, value), "r") as file:
                    yamlcontent = file.read()
                    if self.safe:
                        conf = yaml.safe_load(yamlcontent)
                    else:
                        conf = yaml.load(yamlcontent)
                del array[key]
                
                array = array_merge_recursive(array, self.process(conf))
        return array
