LogStash::PLUGIN_REGISTRY.add(:modules, "rsystem", LogStash::Modules::Scaffold.new("rsystem", File.join(File.dirname(__FILE__), "..", "configuration")))
