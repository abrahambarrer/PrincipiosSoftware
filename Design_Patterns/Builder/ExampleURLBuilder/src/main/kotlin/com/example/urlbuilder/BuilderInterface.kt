package com.example.urlbuilder

interface BuilderInterface {
    fun setProtocol(protocol:String): BuilderInterface
    fun setHostname(hostname:String): BuilderInterface
    fun setPort(port:String): BuilderInterface
    fun addPath(path:String): BuilderInterface
    fun addQueryParam(key:String, value:String): BuilderInterface
    fun build(): String
}