LogStash::PLUGIN_REGISTRY.add(:modules, "winsystem", LogStash::Modules::Scaffold.new("winsystem", File.join(File.dirname(__FILE__), "..", "configuration")))
