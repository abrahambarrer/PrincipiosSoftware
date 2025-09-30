package com.example.urlbuilder
import kotlin.collections.mutableListOf
import java.net.URLEncoder
import java.nio.charset.StandardCharsets

class URLBuilder : BuilderInterface {
    private var protocol:String? = null
    private var hostName:String? = null
    private var port:String? = null
    private var paths: MutableList<String> = mutableListOf<String>()
    private var queryParams: MutableMap<String, String> = mutableMapOf<String, String>()

    override fun setProtocol(protocol: String): BuilderInterface {
        this.protocol = protocol
        return this
    }

    override fun setHostname(hostname: String): BuilderInterface {
        this.hostName = hostname
        return this
    }

    override fun setPort(port: String): BuilderInterface {
        this.port = port
        return this
    }

    override fun addPath(path: String) = apply {
        paths.add(path)
        return this
    }

    override fun addQueryParam(key: String, value: String) = apply {
        queryParams[key] = value
        return this
    }

    override fun build(): String {
        val url = StringBuilder()

        protocol?.let {url.append("$it://")}
        hostName?.let {url.append(it)}
        port?.let { url.append(":$it") }

        if (paths.isNotEmpty()) {
            paths.forEach { path -> url.append("/$path") }
        }

        if (queryParams.isNotEmpty()) {
            url.append("?")
            val queryString = if (queryParams.isNotEmpty()) {
                queryParams.entries.joinToString("&") {
                    "${encode(it.key)}=${encode(it.value)}"
                }
            } else {
                null
            }
            url.append(queryString)
        }
        return url.toString()
    }

    fun reset(): URLBuilder {
        this.protocol = null
        this.hostName = null
        this.port = null
        this.paths.clear()
        this.queryParams.clear()
        return this
    }

    private fun encode(value: String): String =
        URLEncoder.encode(value, StandardCharsets.UTF_8)
}
