package com.example.urlbuilder

class URLManager(private val builder: URLBuilder) {
    fun buildSecureApiUrl(host: String, version: String, resource: String): String {
        return builder
            .reset()
            .setProtocol("https")
            .setHostname(host)
            .addPath("api")
            .addPath(version)
            .addPath(resource)
            .build()
    }

    fun buildSearchUrl(host: String, query: String, page: Int): String {
        return builder
            .reset()
            .setProtocol("https")
            .setHostname(host)
            .addPath("search")
            .addQueryParam("q", query)
            .addQueryParam("page", page.toString())
            .build()
    }
}